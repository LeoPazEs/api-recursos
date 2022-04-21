from core.my_serializers import DynamicFieldsModelSerializer
from .models import Recurso , Alocacao
from rest_framework import serializers  
from django.utils import timezone
from django.db.models import Q

def validar_periodo_alocacao(pk, data_alocacao, data_devolucao): 
    recurso = Recurso.objects.get(pk = pk) 
    if Alocacao.objects.filter(Q(recurso = recurso) & Q(data_devolucao__gt = timezone.localtime(timezone.now()).date()) & (Q(data_devolucao__gte =  data_alocacao) & Q(data_alocacao__lte = data_devolucao))).exists():
        raise serializers.ValidationError("Periodo de alocação conflita com outro período") 
    return recurso

class AlocacaoSerializer(DynamicFieldsModelSerializer): 
    alocador = serializers.HiddenField(default = serializers.CurrentUserDefault())  
    recurso = serializers.PrimaryKeyRelatedField(read_only = True) 

    def validate(self, data):
        data_alocacao = data["data_alocacao"] 
        data_devolucao = data["data_devolucao"] 
        if data_alocacao > data_devolucao: 
            raise serializers.ValidationError("Data de devolução antes da data de alocacao.") 
        data["recurso"] = validar_periodo_alocacao(self.context['view'].kwargs['pk'], data_alocacao, data_devolucao)
        return data

    class Meta: 
        model = Alocacao 
        fields = ["data_alocacao", "data_devolucao", "alocador", "recurso"]  
  

class RecursoSerializer(DynamicFieldsModelSerializer): 
    alocacoes = AlocacaoSerializer( fields = ("data_alocacao", "data_devolucao", "recurso"), many = True, read_only = True)

    class Meta: 
        model = Recurso 
        fields = ["id", "nome", "alocacoes", "status"]   