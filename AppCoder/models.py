from django.db import models

# Create your models here.

class Curso (models.Model):
    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

class Estudiante (models.Model):
     nombre = models.CharField(max_length=30)
     apellido = models.CharField(max_length=30)
     email = models.EmailField(null=True)

class Profesor (models.Model):
     nombre = models.CharField(max_length=30)
     apellido = models.CharField(max_length=30)
     email = models.EmailField(null=True) 
     profecion = models.CharField(max_length=30, null=True)

class Entregable(models.Model):
     nombre = models.CharField(max_length=30)
     fechaDeEntrega = models.DateField()
     entregado = models.BooleanField()