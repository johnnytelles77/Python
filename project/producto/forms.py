# forms.py
from django import forms

class BuscarProductoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', required=False)
    categoria = forms.CharField(label='Categoría', required=False)
    # Puedes agregar más campos según tus necesidades de búsqueda
