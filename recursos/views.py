from core.my_views import DynamicSerializerListAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView , CreateAPIView
from rest_framework.permissions import IsAdminUser

from .models import Recurso 
from .serializers import RecursoSerializer, AlocacaoSerializer

from rest_framework.response import Response
from rest_framework import status

#Users
# api/recursos/listar-recursos
class RecursosUserListarView(DynamicSerializerListAPIView): 
    queryset = Recurso.objects.disponiveis() 
    serializer_class = RecursoSerializer 
    fields = ("id", "nome", "alocacoes")   

# api/recursos/alocar-recurso/<int:pk>
class AlocarUser(CreateAPIView): 
    serializer_class =  AlocacaoSerializer
    queryset = Recurso.objects.disponiveis() 


    # def perform_create(self, serializer):
    #     recurso = Recurso.objects.get(pk = self.kwargs["pk"])
    #     serializer.save(recurso = recurso)

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


