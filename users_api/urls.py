from django.urls import path 
from .views import UserStaffListarCriarView, UserStaffRecuperarDeletarView

app_name = "users_api"

urlpatterns = [
    #Staff
    path("staff/listar-criar-users/", UserStaffListarCriarView.as_view(), name="listar-criar-users"),
    path("staff/deletar-users/<int:pk>", UserStaffRecuperarDeletarView.as_view(), name="deletar-users")
]