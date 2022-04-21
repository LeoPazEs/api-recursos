

from core.my_views import DynamicSerializerListAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView , CreateAPIView
from rest_framework.permissions import IsAdminUser

from .models import Recurso 
from .serializers import RecursoSerializer, AlocacaoSerializer

from rest_framework import status
from django.db.models import ProtectedError
from rest_framework.response import Response

#Users
# api/recursos/listar-recursos
class RecursosUserListarView(DynamicSerializerListAPIView): 
    queryset = Recurso.objects.disponiveis() 
    serializer_class = RecursoSerializer 
    fields = ("id", "nome", "alocacoes")   

# api/recursos/alocar-recurso/<int:pk>
class RecursoUserAlocar(CreateAPIView): 
    serializer_class =  AlocacaoSerializer
    queryset = Recurso.objects.disponiveis() 

# STAFF
# api/recursos/staff/listar-criar-recursos/
class RecursosStaffListarCriarView(ListCreateAPIView): 
    permission_classes = [IsAdminUser]
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer 

# api/recursos/staff/recuperar-editar-deletar/<int:pk>/
class RecursosStaffRecuperarDeletarEditarView(RetrieveUpdateDestroyAPIView): 
    permission_classes = [IsAdminUser]
    serializer_class = RecursoSerializer  
    queryset = Recurso.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            self.perform_destroy(instance) 
        except ProtectedError as e: return Response(data= {"Recurso protegido" : "Recurso não pode ser deletado porque é protegido, provavelmente existem alocações relacionadas ao recurso."} ,status = status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)

    

