from django.shortcuts import render
from django.http import HttpResponse
from AppTicket.forms import SoliciForm
from .models import Solicitud
#from .templates import solicitudForm

# Create your views here.

#def inicio(request):
#    return HttpResponse("Hola desde inicio")

def inicio(request):
    return render(request, "AppTicket/inicio.html")

def solicitud(request):
    return render(request, "AppTicket/solicitud.html")

def solucion(request):
    return render(request, "AppTicket/solucion.html")

def reporte(request):
    return render(request, "AppTicket/reporte.html")

def usuario(request):
    return render(request, "AppTicket/usuario.html")    

#def solicitudesForm(request):
 #   if request.method=="POST":
  #      titulo= request.POST["titulo"]
   #     detalle= request.POST["detalle"]
    #    solicitudes= Solicitudes(titulo=titulo, detalle=detalle)
     #   solicitudes.save()
      #  return render(request, "AppTicket/inicio.html", {"mensaje": "Solicitud Guardada Correctamente"})
    #else:
     #   return render(request, "AppTicket/solicitudesForm.html")


def solicitudFormularioVista(request):
    if request.method=="POST":
        formulario= SoliciForm(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            asunto= info["asunto"]
            nombre= info["nombre"]
            apellido= info["apellido"]
            descripcion= info["descripcion"]
            solicitud= Solicitud(asunto=asunto, nombre=nombre, apellido=apellido, descripcion=descripcion)
            solicitud.save()
            
            return render(request, "AppTicket/inicio.html", {"mensaje": "informacion guardada"})
        else:
            return render(request, "AppTicket/solicitudForm.html", {"formulario": formulario, "mensaje": "informacion no valida"})
    else:
        formulario= SoliciForm()
        return render(request, "AppTicket/solicitudForm.html", {"formulario": formulario})



        
		