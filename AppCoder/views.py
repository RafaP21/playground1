from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import *
from .forms import CursoFormulario, ProfesorFormulario
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
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
   
   
   
def listaProfesores (req):
       profesores = Profesor.objects.all()
       return render(req, "leerProfesores.html", {"profesores" : profesores})


def creaProfesor(req):
    if req.method == "POST":
         miformulario = ProfesorFormulario(req.POST)
         
         if miformulario.is_valid():
             print(miformulario.cleaned_data)
             data = miformulario.cleaned_data
             profesor= Profesor(nombre= data["nombre"], apellido=data["apellido"], email= data["email"], profecion=data["profecion"])
             profesor.save()
             return render(req, "inicio.html", {"mensaje": "Profesor creado con exito"})
       
         else: 
             return render(req, "inicio.html", {"mensaje": "Formulario invalido"})
         
    else:
        
        miformulario = ProfesorFormulario() 
        return render(req, "profesor_formulario.html", {"miformulario" :  miformulario})
    

def eliminarProfesor(req,id):

    if req.method == "POST":
        profesor = Profesor.objects.get(id=id)
        profesor.delete()
        
        profesores = Profesor.objects.all()
        return render(req, "leerProfesores.html", {"profesores"  : profesores})


def editarProfesor (req,id):
   profesor = Profesor.objects.get(id=id)

   if req.method == "POST":
         miformulario = ProfesorFormulario(req.POST)
         
         if miformulario.is_valid():
             print(miformulario.cleaned_data)
             data = miformulario.cleaned_data
             profesor.nombre = data["nombre"]
             profesor.apellido = data["apellido"]
             profesor.email = data["email"]
             profesor.profecion = data["profecion"]
             profesor.save()
             return render(req, "inicio.html", {"mensaje": "Profesor actualizado con exito"})
       
         else: 
             return render(req, "inicio.html", {"mensaje": "Formulario invalido"})
         
   else:
        
        miformulario = ProfesorFormulario(initial={
            "nombre": profesor.nombre,
            "aprellido": profesor.apellido,
            "email": profesor.email,
            "profecion": profesor.profecion,

        }) 
        return render(req, "editarProfesor.html", {"miformulario" :  miformulario , "id" : profesor.id})
  


class CursoList(ListView):
    model = Curso
    template_name = "Curso_list.html"
    context_object_name = "cursos"


class CursoDetail(DetailView):
    model = Curso
    template_name = "Curso_detail.html"
    context_object_name = "curso"


class CursoCreate(CreateView):
    model = Curso
    template_name = "Curso_create.html"
    fields = ["nombre", "camada"]
    success_url = "/AppCoder/"


class CursoUpdate(UpdateView):
    model = Curso
    template_name = "Curso_update.html"
    fields = ("__all__")
    success_url = "/AppCoder/"
    
class CursoDelete(DeleteView):
    model = Curso
    template_name = "Curso_delete.html"
    success_url = "/AppCoder/"    

def loginUsuario (req): 
    
    if req.method == "POST":
        
        miFormulario = AuthenticationForm(req, data= req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user= authenticate(username=usuario, password=psw)

            if user is not None:
                login(req,user)
                return render(req,"inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render (req, "inicio.html", {"mensaje": "Datos Incorrectos"})
        else : 
            return render (req, "inicio.html", {"mensaje": "Formulario Invalido"})
        
        
    else: 
            miFormulario = AuthenticationForm()
            return render (req, "login.html", {"miFormulario" : miFormulario})    


