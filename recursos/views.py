

from core.my_views import DynamicSerializerListAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView , CreateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAdminUser

from .models import Recurso 
from .serializers import RecursoSerializerUser, RecursoSerializerStaff, AlocacaoSerializer

from rest_framework import status
from django.db.models import ProtectedError
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiResponse

#Users
# api/recursos/listar-recursos
class RecursosUserListarView(DynamicSerializerListAPIView): 
    queryset = Recurso.objects.disponiveis() 
    serializer_class = RecursoSerializerUser 
    fields = ("id", "nome", "alocacoes", "data_maxima_alocacao")   

@extend_schema_view(
    post= extend_schema(
        summary="Cria uma nova alocação para o recurso com id na url.",
        responses={
            201: OpenApiResponse(response= AlocacaoSerializer,
                                 description='Criou uma nova alocação para o recurso com o id na url.'),
            400: OpenApiResponse(description='Retorna non_field_errors para recursos inválidos ou períodos inválidos para recurso. Retorna "nome_do_field": "menssagem de erro" caso o erro for de um field específico. '),
        },
    )
)
# api/recursos/alocar-recurso/<int:pk>
class RecursoUserAlocar(CreateAPIView): 
    serializer_class =  AlocacaoSerializer
        

# STAFF
# api/recursos/staff/listar-criar-recursos/
@extend_schema_view(
    post= extend_schema(
        summary="Status recebe D ou I de disponível e indisponível respectivamente e o periodo máximo de alocação deve ser em dias.",
    )
)
class RecursosStaffListarCriarView(ListCreateAPIView): 
    permission_classes = [IsAdminUser]
    queryset = Recurso.objects.all()   
    serializer_class = RecursoSerializerStaff
    

@extend_schema_view(
    delete= extend_schema(
        responses={
            204: OpenApiResponse(description='No response body.'),
            400: OpenApiResponse(description='Retorna recurso protegido caso existam alocações para aquele recurso.')
        },
    )
)
# api/recursos/staff/recuperar-editar-deletar/<int:pk>/
class RecursosStaffRecuperarDeletarEditarView(RetrieveUpdateDestroyAPIView): 
    permission_classes = [IsAdminUser]
    serializer_class = RecursoSerializerStaff  
    queryset = Recurso.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            self.perform_destroy(instance) 
        except ProtectedError as e: return Response(data= {"Recurso protegido." : "Recurso não pode ser deletado porque é protegido, provavelmente existem alocações relacionadas ao recurso."} ,status = status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)

    

