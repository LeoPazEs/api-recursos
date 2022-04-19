from core.my_views import DynamicSerializerListAPIView, DynamicSerializerUpdateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
from rest_framework.permissions import IsAdminUser

from .models import Recurso 
from .serializers import RecursoSerializer

#Users
# api/recursos/listar-recursos
class RecursosUserListarView(DynamicSerializerListAPIView): 
    queryset = Recurso.objects.recursos_disponiveis() 
    serializer_class = RecursoSerializer 
    fields = ("nome",)   

# api/recursos/alocar-recurso/<int:pk>
class RecursosUserEditar(DynamicSerializerUpdateAPIView): 
    serializer_class = RecursoSerializer  
    queryset = Recurso.objects.recursos_disponiveis()
    fields = ("data_alocacao","data_desalocacao")
 
# STAFF
# api/recursos/listar-criar-recursos/
class RecursosStaffListarCriarView(ListCreateAPIView): 
    permission_classes = [IsAdminUser]
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer 

# api/recursos/recuperar-editar-deletar/<int:pk>/
class RecursosStaffRecuperarDeletarEditarView(RetrieveUpdateDestroyAPIView): 
    permission_classes = [IsAdminUser]
    serializer_class = RecursoSerializer  
    queryset = Recurso.objects.all()


