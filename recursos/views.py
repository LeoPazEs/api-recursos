from core.my_views import DynamicSerializerListAPIView 
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Recurso 
from .serializers import RecursoSerializer

# api/recursos/listar-recursos
class RecursosUserListarView(DynamicSerializerListAPIView): 
    queryset = Recurso.objects.recursos_disponiveis() 
    serializer_class = RecursoSerializer 
    fields = ("nome",)  

 
# STAFF
# api/recursos/listar-criar-recursos/
class RecursosStaffListarCriarView(ListCreateAPIView): 
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer 

# api/recursos/recuperar-editar-deletar/<int:pk>/
class RecursosStaffRecuperarDeletarEditarView(RetrieveUpdateDestroyAPIView): 
    serializer_class = RecursoSerializer  
    queryset = Recurso.objects.all()


