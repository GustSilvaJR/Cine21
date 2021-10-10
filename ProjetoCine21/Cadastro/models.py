from django.db import models
from django.contrib.auth.models import(BaseUserManager, AbstractBaseUser, PermissionsMixin)

# Create your models here.

#INICO-MODEL-USUARIO
class UsuarioManager(BaseUserManager):
    def create_user(self,email,password=None):
        usuario = self.model(
            email = email
        )

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)

        usuario.save()

        return usuario 

    def create_superuser(self,email,password):   
        usuario = self.create_user(
            email = email,
            password = password,
        ) 

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)

        usuario.save()
        
        return usuario 
class Usuario(AbstractBaseUser, PermissionsMixin):
    GENERO = [
        ("M", "Masculino" ),
        ("F", "Feminino"),
        ("A", "Alienígena"),
    ]

    nome = models.CharField('Nome do Usuário', max_length=100, null = False, blank=False)

    username = models.CharField('UserName', unique=True, max_length=30, null=False, blank=False)

    email = models.EmailField('E-mail', unique=True, max_length=100, null=False, blank=False)

    genero = models.CharField('Genero', max_length=40, choices= GENERO)

    is_active = models.BooleanField(verbose_name="Usuário está ativo",default=True)

    is_staff  = models.BooleanField(verbose_name="Usuário é da equipe de desenvolvimento", default= False)

    is_superuser = models.BooleanField(verbose_name= "Usuário é um superusuario",default=False)

    USERNAME_FIELD = "email"
    objects = UsuarioManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def meuRetorno(self):
        return str(self.nome +' '+ self.username)
#-------------------------FIM-MODEL-USUARIO

#INICIO-MODEL-ANIME