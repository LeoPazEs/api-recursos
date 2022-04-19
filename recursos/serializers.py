from core.my_serializers import DynamicFieldsModelSerializer
from .models import Recurso 

class RecursoSerializer(DynamicFieldsModelSerializer): 
    class Meta: 
        model = Recurso 
        fields = "__all__" 