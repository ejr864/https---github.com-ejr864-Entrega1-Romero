from django import forms

class SoliciForm(forms.Form):
    asunto= forms.CharField(label="asunto", max_length=50)
    nombre= forms.CharField(label="nombre", max_length=50)
    apellido= forms.CharField(label="apellido", max_length=50)
    descripcion= forms.CharField(label="descripcion", max_length=50)
