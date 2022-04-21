from django.db import models
from django.contrib.auth.models import User

from django.db.models import Q
from .validators import validatar_data_futuro

STATUS_CHOICES = [
    ("D", "Disponível"), 
    ("I", "Indisponível"),
]

class Recurso(models.Model): 

    class RecursosManager(models.Manager):  
        def disponiveis(self):
            return self.filter(Q(status = "D"))  
 
    nome = models.CharField(max_length= 200) 
    status = models.CharField(max_length= 1,choices = STATUS_CHOICES, default = "D")

    objects = RecursosManager()

    def __str__(self) -> str:
        return self.nome 

    class Meta: 
        ordering = ['-id'] 
    
class Alocacao(models.Model): 
    alocador = models.ForeignKey(User, on_delete= models.PROTECT) 
    data_alocacao = models.DateField(validators=[validatar_data_futuro]) 
    data_devolucao = models.DateField(validators=[validatar_data_futuro])  
    recurso = models.ForeignKey(Recurso, on_delete= models.PROTECT, related_name="alocacoes")
