from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id)
