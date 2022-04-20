from django.urls import path
from .views import RecursosUserListarView, RecursosStaffListarCriarView, RecursosStaffRecuperarDeletarEditarView, AlocarUser

app_name = "recursos"

urlpatterns = [
    #User
    path("listar-recursos/", RecursosUserListarView.as_view(), name= "recursos-listar-user"), 
    path("alocar-recurso/<int:pk>/", AlocarUser.as_view(), name =  "recursos-recuperar-editar-deletar"),

    #Staff
    path("staff/listar-criar-recursos/", RecursosStaffListarCriarView.as_view(), name = "recursos-listar-criar-staff"),
    path("staff/recuperar-editar-deletar/<int:pk>/", RecursosStaffRecuperarDeletarEditarView.as_view(), name =  "recursos-recuperar-editar-deletar") 
]
