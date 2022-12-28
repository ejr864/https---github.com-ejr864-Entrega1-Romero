from django.contrib import admin
from .models import Reporte, Solicitud, Usuario, Solucion

# Register your models here.
admin.site.register(Reporte)
admin.site.register(Solicitud)
admin.site.register(Usuario)
admin.site.register(Solucion)
