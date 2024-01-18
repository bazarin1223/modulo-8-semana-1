from django.contrib import admin
from base.models import contatom
from django.contrib import messages
@admin.action(description='marcar formulario(s) de contato como lido(s)')
def marcar_como_lido(modeladmin,request,queryset):
    queryset.update(lido=True)
    modeladmin.message_user(request,'formulario (s) de contato(s) como lido(s)',messages.SUCCESS)












@admin.register(contatom)
class contatoadmin(admin.ModelAdmin):
    list_display = ['nome','email','data']
    search_fields = ['nome','email']
    list_filter = ['data','lido']
    actions = [marcar_como_lido]

