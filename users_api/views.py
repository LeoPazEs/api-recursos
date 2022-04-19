from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView

# api/users/listar-criar-users/
class UserStaffListarCriarView(ListCreateAPIView): 
    queryset = User.objects.all()
    serializer_class = UserSerializer