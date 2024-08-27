# Create your views here.
# views.py
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from .models import Mensajes

def base(request):
    if request.method == 'POST':
        mensajes = Mensajes.objects.filter(destinatario=request.POST.get('destinatarios'))
        return render(request, 'Mensajes/show_mensajes.html', {'mensajes': mensajes})
    else:
        form = ListarDestinatarios()
    return render(request, 'Mensajes/base.html', {'destinatarios': form})
    
#def show_mensajes(request):
#
#    mensajes = Mensajes.objects.filter(destinatario='Franco')
#    return render(request, 'Mensajes/show_mensajes.html', {'destinatarios': mensajes})
    

class ListarDestinatarios(forms.Form):
    nombres_destinatarios = [(mensaje, mensaje) for mensaje in Mensajes.objects.values_list('destinatario', flat=True).distinct()]

    destinatarios = forms.ChoiceField(
        choices=nombres_destinatarios,
        widget=forms.Select,
    )
