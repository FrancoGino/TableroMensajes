# Importa HttpResponse para manejar respuestas HTTP y render para renderizar plantillas HTML.
# Importa forms de Django para definir formularios.
# Importa el modelo Mensajes de la aplicación actual.

from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from .models import Mensajes

# Definición de la vista base
def base(request):
    # Crea una instancia del formulario ListarDestinatarios
    form = ListarDestinatarios()
    # Define un contexto que incluye el formulario y una URL
    context = {
        'form': form,
        'url': 'http://localhost:8000/mensajes/recibidos/',
    }
    # Renderiza la plantilla 'Mensajes/base.html' con el contexto proporcionado
    return render(request, 'Mensajes/base.html', context)

# Definición de la vista show_mensajes
def show_mensajes(request):
    # Obtiene el destinatario específico desde los parámetros de la solicitud GET
    destinatario = request.GET.get('destinatarios')
    # Filtra los mensajes para un destinatario específico
    mensajes = Mensajes.objects.filter(destinatario=destinatario)
    # Renderiza la plantilla 'Mensajes/show_mensajes.html' con los mensajes y el destinatario en el contexto
    return render(request, 'Mensajes/show_mensajes.html', {'mensajes': mensajes, 'destinatario': destinatario})

# Definición del formulario ListarDestinatarios
class ListarDestinatarios(forms.Form):
    # Obtiene una lista de destinatarios únicos de la base de datos
    nombres_destinatarios = [(mensaje, mensaje) for mensaje in Mensajes.objects.values_list('destinatario', flat=True).distinct()]

    # Define un campo de formulario de tipo select con las opciones obtenidas en la consulta
    destinatarios = forms.ChoiceField(
        choices=nombres_destinatarios,
        widget=forms.Select,
    )
