from django import forms
from . import models

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ["nombre", "apellido", "nacimiento", "pais_origen"]

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        apellido = cleaned_data.get("apellido")

        # Verificar si ya existe un cliente con el mismo nombre y apellido
        if models.Cliente.objects.filter(nombre=nombre, apellido=apellido).exists():
            raise forms.ValidationError("Este cliente ya está registrado. Intente con otro nombre o apellido.")

        return cleaned_data
