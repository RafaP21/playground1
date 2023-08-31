from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Curso
from .forms import CursoFormulario
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
    return render(req, "inicio.html")


def cursos(req):
    return render(req, "cursos.html")

def profesores(req):
    return render(req, "profesores.html")


def estudiantes(req):
    return render(req, "estudiantes.html")


def entregables (req):
    return render(req, "entregables.html")


def curso_formulario(req : HttpRequest):
    print('method', req.method)
    print('post', req.POST)
    if req.method == "POST":
         miformulario = CursoFormulario(req.POST)
         
         if miformulario.is_valid():
             print(miformulario.cleaned_data)
             data = miformulario.cleaned_data
             curso= Curso(nombre= data["curso"], camada=data["camada"])
             curso.save()
             return render(req, "inicio.html", {"mensaje": "curso creado con exito"})
       
         else: 
             return render(req, "inicio.html", {"mensaje": "formulario invalido"})
         
    else:
        
        miformulario = CursoFormulario() 
        return render(req, "curso_formulario.html", {"miformulario" :  miformulario})
    
def busqueda_camada(req):
    return render (req, "busquedaCamada.html")

def buscar(req):
    
   if req.GET["camada"]:
        camada = req.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)
        if cursos:
            return render(req, "resultado.html", {"cursos": cursos})
    
   else:
        return HttpResponse('No escribiste ninguna camada')