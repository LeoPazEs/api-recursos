from core.my_serializers import DynamicFieldsModelSerializer
from .models import Recurso , Alocacao
from rest_framework import serializers  

from datetime import datetime


class RecursoSerializer(DynamicFieldsModelSerializer): 
    alocacoes = serializers.PrimaryKeyRelatedField(many = True, read_only= True)

    class Meta: 
        model = Recurso 
        fields = ["id", "nome", "alocacoes"]   

class AlocacaoSerializer(serializers.ModelSerializer): 
    alocador = serializers.HiddenField(default = serializers.CurrentUserDefault())  
    recurso = serializers.PrimaryKeyRelatedField(read_only= True)
    
    

    class Meta: 
        model = Alocacao 
        fields = ["data_alocacao", "data_devolucao", "alocador", "recurso"]   