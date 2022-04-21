from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser, AllowAny

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