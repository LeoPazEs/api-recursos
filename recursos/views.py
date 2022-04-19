from core.my_views import DynamicSerializerListAPIView 
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Recurso 
from .serializers import RecursoSerializer

class RecursosUserListarView(DynamicSerializerListAPIView): 
    queryset = Recurso.objects.recursos_disponiveis() 
    serializer_class = RecursoSerializer 
    fields = ("nome")  

class RecursosStaffListarCriarView(ListCreateAPIView): 
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer 

class RecursosStaffListarCriarView(RetrieveUpdateDestroyAPIView): 
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer

