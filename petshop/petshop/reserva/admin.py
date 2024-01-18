from django.contrib import admin
from reserva.models import reserva

@admin.register(reserva)
class reservaadmin(admin.ModelAdmin):
    list_display = ['nome', 'email','nome_do_pet','data','turno']
    search_fields = ['nome','email','nome_do_pet']
    list_display = ['data','turno','tamanho']
