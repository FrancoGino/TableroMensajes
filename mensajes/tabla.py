import django_tables2 as tables
from .models import Mensajes

class MensajesTabla(tables.Table):
    class Meta:
        model = Mensajes
        template_name = "django_tables2/bootstrap.html"
        fields = ("remitente", "texto", "fecha_hora")
