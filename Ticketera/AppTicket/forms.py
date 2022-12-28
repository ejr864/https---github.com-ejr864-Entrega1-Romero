from django import forms

class SoliciForm(forms.Form):
    asunto= forms.CharField(label="asunto", max_length=50)
    nombre= forms.CharField(label="nombre", max_length=50)
    apellido= forms.CharField(label="apellido", max_length=50)
    descripcion= forms.CharField(label="descripcion", max_length=50)


class UserForm(forms.Form):
    nombre= forms.CharField(label="nombre", max_length=50)
    apellido= forms.CharField(label="apellido", max_length=50)
    cargo= forms.CharField(label="cargo", max_length=50)
    email= forms.EmailField(label="email", max_length=50)


class SolFor(forms.Form):
    titulo= forms.CharField(label="titulo", max_length=50)
    detalle= forms.CharField(label="detalle", max_length=50)
