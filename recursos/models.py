from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from .validators import validatar_data_futuro

STATUS_CHOICES = [
    ("D", "Disponível"), 
    ("I", "Indisponível"),
]

class Recurso(models.Model): 

    class RecursosManager(models.Manager):  
        def disponiveis(self):
            return self.filter(status = "D", data_maxima_alocacao__gte = timezone.localtime(timezone.now()).date())  
 
    nome = models.CharField(max_length= 200) 
    status = models.CharField(max_length= 1,choices = STATUS_CHOICES, default = "D")
    data_maxima_alocacao = models.DateField() 
    periodo_maximo_alocacao = models.PositiveIntegerField(null= True)

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
