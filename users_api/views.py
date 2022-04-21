from .serializers import UserSerializer
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import serializers
from drf_spectacular.utils import extend_schema, inline_serializer, extend_schema_view, OpenApiResponse
#  api/users/criar-user/
class UserCriarView(CreateAPIView): 
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer 


#Staff
# api/users/staff/listar-criar-users/
class UserStaffListarCriarView(ListCreateAPIView): 
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer 

# api/users/staff/deletar-users/
class UserStaffRecuperarDeletarView(RetrieveDestroyAPIView): 
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer 

@extend_schema_view(post =  extend_schema( 
        request= inline_serializer(name = "refresh_token", fields= {"refresh_token" : serializers.CharField()}),
        responses= {
            200: OpenApiResponse(description='No response body.'),
            400: OpenApiResponse(description='Refresh token não fornecido.')
        }
    ))
# api/users/logout/
class BlackListTokenView(APIView): 
    permission_classes = [AllowAny] 

    def post(self, request): 
        try: 
            refresh_token = request.data['refresh_token'] 
            token = RefreshToken(refresh_token) 
            token.blacklist() 
        except Exception: 
            return Response(status= status.HTTP_400_BAD_REQUEST) 
        return Response(status = status.HTTP_200_OK)
