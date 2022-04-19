from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
from django.db.models import Q
from .validators import validatar_data_desalocacao

class Recurso(models.Model): 

    class RecursosManager(models.Manager):  
        def recursos_disponiveis(self):
            data_atual = datetime.now()
            return self.filter(Q(data_alocacao__gt = data_atual) | Q(data_desalocacao__lt = data_atual) | Q(data_alocacao = None) & Q(data_desalocacao = None))

        def recursos_indisponiveis(self): 
            data_atual = datetime.now() 
            return self.filter(Q(data_alocacao__lt = data_atual) | Q(data_desalocacao__gt = data_atual))  

    user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True) 
    nome = models.CharField(max_length= 200) 
    data_alocacao = models.DateField(null = True) 
    data_desalocacao = models.DateField(null = True, validators=[validatar_data_desalocacao]) 

    objects = RecursosManager()

    def __str__(self) -> str:
        return self.nome 

    class Meta: 
        ordering = ['-id']