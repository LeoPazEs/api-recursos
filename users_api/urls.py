from django.urls import path 
from .views import UserStaffListarCriarView, UserStaffRecuperarDeletarView, UserCriarView

app_name = "users_api"

urlpatterns = [
    #Any 
    path("registrar/", UserCriarView.as_view(), name="criar_user"),

    #Staff
    path("staff/listar-criar-users/", UserStaffListarCriarView.as_view(), name="listar-criar-users"),
    path("staff/deletar-users/<int:pk>", UserStaffRecuperarDeletarView.as_view(), name="deletar-users")
]