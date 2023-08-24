from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso
# Create your views here.

def curso(req, nombre, camada):
    curso= Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f"""
        <p>Curso: {curso.nombre} - Camada: {curso.camada} agregado!! </p>
        """)  

def lista_Cursos(req):
    lista = Curso.objects.all()

    return render(req,"lista_cursos.html", {"lista_cursos" : lista})

def inicio(req):
    return HttpResponse("vista inicio")


def cursos(req):
    return HttpResponse("vista cursos")


def profesores(req):
    return HttpResponse("vista profesores")


def estudiantes(req):
    return HttpResponse("vista estudiantes")


def entregables (req):
    return HttpResponse("vista entregables")
