# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('mensajes/recibidos/', views.show_mensajes, name='mensajes_recibidos'),
]