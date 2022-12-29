from django.shortcuts import render
from django.http import HttpResponse
from AppTicket.forms import SoliciForm, UserForm, SolFor
from .models import Solicitud, Usuario, Solucion
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




def UsuarioFormularioVista(request):
    if request.method=="POST":
        formulario= UserForm(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            nombre= info["nombre"]
            apellido= info["apellido"]
            cargo= info["cargo"]
            email= info["email"]
            usuario= Usuario(nombre=nombre, apellido=apellido, cargo=cargo, email=email)
            usuario.save()
            return render(request, "AppTicket/inicio.html", {"mensaje": "informacion guardada"})
        else:
            return render(request, "AppTicket/formUsuario.html", {"formulario": formulario, "mensaje": "informacion no valida"})
    else:
        formulario= UserForm()
        return render(request, "AppTicket/formUsuario.html", {"formulario": formulario})


    
def SolucionFormularioVista(request):
    if request.method=="POST":
        formulario= SolFor(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            titulo= info["titulo"]
            detalle= info["detalle"]
            solucion= Solucion(titulo=titulo, detalle=detalle)
            solucion.save()
            return render(request, "AppTicket/inicio.html", {"mensaje": "informacion guardada"})
        else:
            return render(request, "AppTicket/formSolu.html", {"formulario": formulario, "mensaje": "informacion no valida"})
    else:
        formulario= SolFor()
        return render(request, "AppTicket/formSolu.html", {"formulario": formulario})



def buscar(request):
    
    usuario= request.GET["nombre"]
    if usuario!="":
        usuario = Usuario.objects.filter(nombre__icontains=usuario)
        return render(request, "AppCoder/resultadoBusqueda.html", {"usuario": usuario})
    else:
        return render(request, "AppCoder/busquedaUser.html", {"mensaje": "Che Ingresa una comision para buscar!"})
        
		