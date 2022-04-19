from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAdminUser

#Staff
# api/users/listar-criar-users/
class UserStaffListarCriarView(ListCreateAPIView): 
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer 

# api/users/deletar-users/
class UserStaffRecuperarDeletarView(RetrieveDestroyAPIView): 
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer