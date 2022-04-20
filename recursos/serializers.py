from core.my_serializers import DynamicFieldsModelSerializer
from .models import Recurso , Alocacao
from rest_framework import serializers  

from datetime import datetime

class AlocacaoSerializer(DynamicFieldsModelSerializer): 
    alocador = serializers.HiddenField(default = serializers.CurrentUserDefault())  
    recurso = serializers.PrimaryKeyRelatedField(read_only = True) 

    def validate(self, data):
        data_alocacao = data["data_alocacao"] 
        data_devolucao = data["data_devolucao"] 
        print(self.context['view'].kwargs['pk'])
        if data_alocacao > data_devolucao: 
            raise serializers.ValidationError("Data de devolução antes da data de alocacao.") 
        recurso = Recurso.objects.get(pk = self.context['view'].kwargs['pk']) 
        alocacoes_ativas = Alocacao.objects.filter(recurso = recurso, data_devolucao__gt = datetime.now()) 
        for alocacao in alocacoes_ativas: 
            if  alocacao.data_alocacao >= data_alocacao or alocacao.data_devolucao <= data_devolucao: 
                raise serializers.ValidationError("Periodo de alocação conflita com outro período") 
        data["recurso"] = recurso
        return data

    class Meta: 
        model = Alocacao 
        fields = ["data_alocacao", "data_devolucao", "alocador", "recurso"]  
  

class RecursoSerializer(DynamicFieldsModelSerializer): 
    alocacoes = AlocacaoSerializer( fields = ("data_alocacao", "data_devolucao"), many = True,)

    class Meta: 
        model = Recurso 
        fields = ["id", "nome", "alocacoes"]   