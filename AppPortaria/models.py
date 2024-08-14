from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



    
class Veiculo(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)  
    cor = models.CharField(max_length=30)
    placa = models.CharField(max_length=7, unique=True)
    nome_do_condutor = models.CharField(max_length=100)  
    categoria = models.CharField(max_length=50)  
    modelo = models.CharField(max_length=255, default= False)
    veiculo_institucional = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.tipo} - {self.placa}"
    
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=14, unique=True)  
    nome = models.CharField(max_length=100)  
    função = models.CharField(max_length=50)  
    setor = models.CharField(max_length=50)  
    password = models.CharField(max_length=20)  
    is_admin = models.BooleanField(default=False)
    user = models.OneToOneField(User, null=True , on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
   
    
    def __str__(self):
        return self.nome
    

class Movimento(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    id = models.AutoField(primary_key=True)
    data = models.DateTimeField( auto_now_add=True)
    km_entrada = models.IntegerField(null=True, blank=True)
    km_saida = models.IntegerField(null=True, blank=True)
    entrada = models.CharField(max_length=50)  
    saida = models.CharField(max_length=50)  

    def __str__(self):
        return f"{self.veiculo} - {self.placa}"
   