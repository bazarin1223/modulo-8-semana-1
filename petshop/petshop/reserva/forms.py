from django import forms
from reserva.models import reserva
from datetime import date

class reservaform(forms.ModelForm):
    def clean_data(self):
        data = self.cleaned_data['data']
        hoje = date.today()
        if data < hoje:
            raise forms.ValidationError('não é possivel realizar uma reserva para o passado!')
        
        if data:
            reserva_para_o_dia = reserva.objects.filter(data=data).count()
            if reserva_para_o_dia >=4:
                raise forms.ValidationError('ja exixte 4 reserva para esse dia escolha outra data!')
        return data 
   
        
    class Meta:
        model = reserva
        fields = [
        'nome','email','data','turno',
        'tamanho','observaçoes'
        ]
        widgets = { 
            'data':forms.DateInput(attrs={'type':'date'}),
         }