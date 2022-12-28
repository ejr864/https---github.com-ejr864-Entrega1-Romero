from django.db import models

# Create your models here.

class Solicitud(models.Model):
    asunto= models.CharField(max_length=50, null=True)
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    descripcion= models.CharField(max_length=50, null=True) 

class Solucion(models.Model):
    titulo= models.CharField(max_length=50)
    detalle= models.CharField(max_length=50)

class Reporte(models.Model):
    titulo= models.CharField(max_length=50)
    detalle= models.CharField(max_length=50)

class Usuario(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    cargo= models.CharField(max_length=50)
    email= models.EmailField()