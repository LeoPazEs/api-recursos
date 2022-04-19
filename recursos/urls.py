from django.urls import path
from .views import RecursosUserListarView, RecursosStaffListarCriarView

app_name = "recursos"

urlpatterns = [
    #User
    path("listar-recursos/", RecursosUserListarView.as_view(), name= "recursos-listar-user"), 

    #Staff
    path("listar-criar-recursos/", RecursosStaffListarCriarView.as_view(), name = "recursos-listar-criar-staff")
]
