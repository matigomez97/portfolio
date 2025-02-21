from django.shortcuts import render
from .models import Proyecto

def proyectos(request):
    proyectos = Proyecto.objects.all()  # Obtener todos los proyectos
    return render(request, 'proyectos.html', {'proyectos': proyectos})
def inicio(request):
    return render(request, 'inicio.html')
def sobre_mi(request):
    return render(request, 'sobre_mi.html')
def contacto(request):
    return render(request, 'contacto.html')