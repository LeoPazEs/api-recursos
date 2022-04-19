from core.my_serializers import DynamicFieldsModelSerializer
from .models import Recurso  
from rest_framework import serializers

class RecursoSerializer(DynamicFieldsModelSerializer): 
    user = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta: 
        model = Recurso 
        fields = "__all__"  

    def save(self, **kwargs):
        """Include default for read_only `user` field"""
        kwargs["user"] = self.fields["user"].get_default()
        return super().save(**kwargs)