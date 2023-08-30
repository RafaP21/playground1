from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('crear-curso/<nombre>/<camada>', curso),
    path('', inicio, name ="inicio"),
    path('profesores/', profesores, name = "profesores"),
    path('estudiantes/',estudiantes, name= "estudiantes"),
    path('entregables/', entregables,name = "entregables"),
    path('lista_cursos/', lista_Cursos, name = "cursos"),
    path ('curso-formulario/', curso_formulario, name = "curso_formulario"),
  

]

