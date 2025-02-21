from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página de inicio
    path('proyectos/', views.proyectos, name='proyectos'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('contacto/', views.contacto, name='contacto'),
]
