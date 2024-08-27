from django.core.management.base import BaseCommand
from mensajes.models import Mensajes

class Command(BaseCommand):
    help = 'Poblar la base de datos'

    def handle(self, *args, **options):
        # Lógica para poblar la base de datos
        obj = Mensajes(remitente=f'Franco',destinatario=f'Enrique',texto='Hola Enrique, ¿sabes de la onda?')
        obj.save()
        obj = Mensajes(remitente=f'Enrique',destinatario=f'Franco',texto='No Franco, hace dias no anda nada')
        obj.save()
        obj = Mensajes(remitente=f'Enrique',destinatario=f'Franco',texto='preguntale a Marco')
        obj.save()
        obj = Mensajes(remitente=f'Franco',destinatario=f'Marco',texto='Hola Marco, enrique me dijo que sabias de la onda')
        obj.save()
        obj = Mensajes(remitente=f'Marco',destinatario=f'Franco',texto='Si Franco, para vos 15K el G')
        obj.save()
        obj = Mensajes(remitente=f'Franco',destinatario=f'Marco',texto='uugghh')
        obj.save()
        
        self.stdout.write(self.style.SUCCESS('Completado.'))