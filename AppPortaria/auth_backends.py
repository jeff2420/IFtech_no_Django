from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import Usuario

class CPFBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        
        usuario = Usuario.objects.get(cpf=username)
        user = usuario.user  # Relacionamento OneToOneField com User
        if user.check_password(senha=password):
            return user
    
    def get_user(self, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return None
