from django.shortcuts import render
from django.http import HttpResponse
from base.forms import contatoform


def inicio(request):
    
    return render(request,'inicio.html')

def contato(request):
    sucesso = False

   
    form = contatoform(request.POST)
    if form.is_valid():
        sucesso = True
        form.save()
         
            

    contexto = {
        'telefone' : '(44)98841-1561',
        'responsavel': 'kaique',
        'form': form,
        'sucesso': sucesso
        
        }
   
    return render(request,'contato.html',contexto)
