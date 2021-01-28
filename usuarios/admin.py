from django.contrib import admin
from .models import Usuarios

# Register your models here.

@admin.register(Usuarios)
class UsuariosAdm(admin.ModelAdmin):
    list_display = ['endereco', 'nome' , 'data_cadastro',]