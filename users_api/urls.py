from django.urls import path 
from .views import UserStaffListarCriarView

app_name = "users_api"

urlpatterns = [
    path("listar-criar-users/", UserStaffListarCriarView.as_view(), name="listar-criar-users")
]