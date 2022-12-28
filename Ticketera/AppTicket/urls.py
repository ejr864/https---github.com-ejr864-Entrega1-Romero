from django.urls import path
from .views import *

urlpatterns = [
    
    #path('curso/', curso),
    #path('cursos/', cursos, name="cursos"),
    #path('estudiantes/', estudiantes, name="estudiantes"),
    #path('profesores/', profesores, name="profesores"),
    #path('entregables/', entregables, name="entregables"),
    path('', inicio, name="inicio"),
    path('solicitud/', solicitud, name="solicitud"),
    path('solucion/', solucion, name="solucion"),
    path('reporte/', reporte, name="reporte"),
    path('usuario/', usuario, name="usuario"),
    path('solicitudForm/', solicitudFormularioVista, name="solicitudForm"),
    ]

