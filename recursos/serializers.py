from core.my_serializers import DynamicFieldsModelSerializer
from .models import Recurso , Alocacao
from rest_framework import serializers  
from django.utils import timezone
from django.db.models import Q

def validar_periodo_alocacao(recurso, data_alocacao, data_devolucao): 
    if recurso.data_maxima_alocacao < data_alocacao: raise serializers.ValidationError({"data_alocacao" :"Data de alocação depois da data máxima."}) 
    if recurso.periodo_maximo_alocacao and recurso.periodo_maximo_alocacao < (data_devolucao - data_alocacao).days :  raise serializers.ValidationError("Período de alocação maior que período máximo.")
    if Alocacao.objects.filter(Q(recurso = recurso) & Q(data_devolucao__gte = timezone.localtime(timezone.now()).date()) & (Q(data_devolucao__gte =  data_alocacao) & Q(data_alocacao__lte = data_devolucao))).exists():
        raise serializers.ValidationError("Período de alocação conflita com outro período.") 
    return recurso

class AlocacaoSerializer(DynamicFieldsModelSerializer): 
    alocador = serializers.HiddenField(default = serializers.CurrentUserDefault())  
    recurso = serializers.PrimaryKeyRelatedField(read_only = True) 

    def validate(self, data):
        data_alocacao = data["data_alocacao"] 
        data_devolucao = data["data_devolucao"] 
        if data_alocacao > data_devolucao: raise serializers.ValidationError("Data de devolução antes da data de alocacao.") 
        try:
            recurso = Recurso.objects.get(pk = self.context['view'].kwargs['pk'], status = "D", data_maxima_alocacao__gte = timezone.localtime(timezone.now()).date())  
        except Recurso.DoesNotExist: 
            raise serializers.ValidationError("Recurso inválido!")

        data["recurso"] = validar_periodo_alocacao(recurso, data_alocacao, data_devolucao)
        return data

    class Meta: 
        model = Alocacao 
        fields = ["id","data_alocacao", "data_devolucao", "alocador", "recurso"]  
  

class RecursoSerializerUser(DynamicFieldsModelSerializer): 
    alocacoes = AlocacaoSerializer( fields = ("data_alocacao", "data_devolucao", "recurso", "id"), many = True, read_only = True) 

    class Meta: 
        model = Recurso 
        fields = ["id", "nome", "status", "alocacoes", "data_maxima_alocacao", "periodo_maximo_alocacao"]    

class  RecursoSerializerStaff(serializers.ModelSerializer): 
    alocacoes = AlocacaoSerializer( fields = ("data_alocacao", "data_devolucao", "recurso", "id"), many = True, read_only = True) 

    class Meta: 
        model = Recurso 
        fields = ["id", "nome", "status", "alocacoes", "data_maxima_alocacao", "periodo_maximo_alocacao"]   