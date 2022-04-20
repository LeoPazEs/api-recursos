from core.my_serializers import DynamicFieldsModelSerializer
from .models import Recurso , Alocacao
from rest_framework import serializers  





class AlocacaoSerializer(serializers.ModelSerializer): 
    alocador = serializers.HiddenField(default = serializers.CurrentUserDefault())  
    recurso = serializers.PrimaryKeyRelatedField(read_only= True)
    
    

    class Meta: 
        model = Alocacao 
        fields = ["data_alocacao", "data_devolucao", "alocador", "recurso"]   

class RecursoSerializer(DynamicFieldsModelSerializer): 
    alocacoes = AlocacaoSerializer(many = True, read_only= True)

    class Meta: 
        model = Recurso 
        fields = ["id", "nome", "alocacoes"]   