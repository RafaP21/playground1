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
    path ('busqueda-camada/', busqueda_camada, name = "busquedaCamada"),
    path ('buscar/', buscar, name = "Buscar"),
    path ('lista-profesores/', listaProfesores, name = "ListaProfesores"),
    path ('profesor-formulario/', creaProfesor, name = "CrearProfesor"),
    path ('elimina-profesor/<int:id>/', eliminarProfesor, name = "EliminaProfesor"),
    path ('editar-profesor/<int:id>/', editarProfesor, name = "EditarProfesor"),
    path ('lista-cursos/', CursoList.as_view(), name = "ListaCursos"),
    path ('detalle-curso/<pk>/', CursoDetail.as_view(), name = "DetallaCursos"),
    path ('crear-cursos/', CursoCreate.as_view(), name = "CreaCursos"),
    path ('actualiza-curso/<pk>/', CursoUpdate.as_view, name = "ActualizaCursos"),
    path ('elimina-curso/<pk>/', CursoDelete.as_view(), name = "EliminaCursos"),

]

