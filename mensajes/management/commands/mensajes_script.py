from django.core.management.base import BaseCommand
from mensajes.models import Mensajes

class Command(BaseCommand):
    help = 'Poblar la base de datos'

    def handle(self, *args, **options):
        # Lógica para poblar la base de datos
        obj = Mensajes(remitente=f'Franco',destinatario=f'Enrique',texto='Hola Enrique, ¿Hiciste el tp necesito ayuda?')
        obj.save()
        obj = Mensajes(remitente=f'Enrique',destinatario=f'Franco',texto='No Franco, no hice nada')
        obj.save()
        obj = Mensajes(remitente=f'Enrique',destinatario=f'Franco',texto='preguntale a Marco')
        obj.save()
        obj = Mensajes(remitente=f'Franco',destinatario=f'Marco',texto='Hola Marco, Me podes dar una mano con el tp')
        obj.save()
        obj = Mensajes(remitente=f'Marco',destinatario=f'Franco',texto='Si Franco, ¿puedo hacer una meet hoy a las 15 te parece?')
        obj.save()
        obj = Mensajes(remitente=f'Franco',destinatario=f'Marco',texto='Si, Muchas gracias')
        obj.save()
        
        self.stdout.write(self.style.SUCCESS('Completado.'))