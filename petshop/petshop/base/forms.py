from django import forms
from base.models import contatom,reservam

class contatoform(forms.ModelForm):
    class Meta:
        model = contatom
        fields = ['nome','email','mensagem']


class reservaform(forms.ModelForm):
    class Meta:
        model = reservam
        fields = ['nome_do_pet','telefone','dia_da_reserva','observaçao']
        widgets = {
            'nome_do_pet': forms.TextInput(
                attrs={
                    'placeholder' : 'Insira o nome do seu pet'
                }
            ),
            'telefone' : forms.TextInput(
                attrs={
                    'placeholder': 'Insira seu telefone aqui'
                }
            ),

            'dia_da_reserva' :forms.TextInput(
                attrs={
                    'placeholder' : 'data da sua reserva'
                }
            )
            
        }
        labels = {
            'nome_do_pet': 'Nome Do Pet ',
            'telefone': 'Telefone ',
            'dia_da_reserva': 'Dia da Reserva ',
            'observaçao' : 'Observação '
        }