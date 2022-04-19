from core.my_serializers import DynamicFieldsModelSerializer
from .models import Recurso  
from rest_framework import serializers  

from datetime import datetime


class RecursoSerializer(DynamicFieldsModelSerializer): 
    user_alocando = serializers.PrimaryKeyRelatedField(source = "user", read_only= True)

    class Meta: 
        model = Recurso 
        fields = ["id", "nome", "user_alocando", "data_alocacao",  "data_desalocacao"]   

class AlocarRecursoSerializer(serializers.ModelSerializer): 
    user = serializers.HiddenField( default=serializers.CurrentUserDefault()) 
    data_alocacao = serializers.HiddenField( default= datetime.now())
    

    class Meta: 
        model = Recurso 
        fields = ["data_alocacao", "data_desalocacao", "user"]   