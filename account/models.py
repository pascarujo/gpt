from django.db import models
from django.conf import settings

from gpt.models import Organizacao


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_nasc = models.DateField(blank=True, null=True, verbose_name='data de nascimento')
    organizacao = models.ForeignKey(Organizacao, on_delete=models.SET_NULL, related_name='membros', blank=True, null=True)

    def __str__(self):
        return f'Perfil do usuário {self.user.username}'