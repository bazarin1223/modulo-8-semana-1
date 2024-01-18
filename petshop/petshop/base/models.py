from django.db import models

# Create your models here.
class contatom(models.Model):
    nome = models.CharField(verbose_name='nome', max_length=50)
    email = models.EmailField(verbose_name='email', max_length=50)
    mensagem = models.TextField(verbose_name='mensagem')
    data = models.DateTimeField(verbose_name='data',auto_now_add=True)
    lido = models.BooleanField(verbose_name='lido',default=False,blank=True)
    def _strs_(selfie):
        return (f'{selfie.nome} [{selfie.email}]')
    class Meta:
        verbose_name = 'formulario de contato'
        verbose_name_plural = 'formulario de contatos'
        ordering = ['-data']


class reservam(models.Model):
    nome_do_pet = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    dia_da_reserva = models.CharField(max_length=50)
    observaçao = models.TextField(verbose_name="observaçao",blank=True)
