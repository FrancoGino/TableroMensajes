# Create your views here.
# views.py
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from .models import Mensajes

def base(request):
    form = ListarDestinatarios()
    context={
        'form': form,
        'url': 'http://localhost:8000/mensajes/recibidos/',
    }
    return render(request, 'Mensajes/base.html', context)
    
def show_mensajes(request):
    mensajes = Mensajes.objects.filter(destinatario=request.GET.get('destinatarios'))
    destinatario = mensajes[0].destinatario
    return render(request, 'Mensajes/show_mensajes.html', {'mensajes': mensajes, 'destinatario': destinatario})
    

class ListarDestinatarios(forms.Form):
    nombres_destinatarios = [(mensaje, mensaje) for mensaje in Mensajes.objects.values_list('destinatario', flat=True).distinct()]

    destinatarios = forms.ChoiceField(
        choices=nombres_destinatarios,
        widget=forms.Select,
    )
