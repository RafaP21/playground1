from django.urls import path
from AppCoder.views import curso,estudiantes,profesores,entregables, inicio, lista_Cursos

urlpatterns = [
    path('crear-curso/<nombre>/<camada>', curso),
    path('', inicio),
    path('profesores/', profesores),
    path('estudiantes/',estudiantes),
    path('entregables/', entregables),
    path('lista_cursos/', lista_Cursos),

]

