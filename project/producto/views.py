# views.py
from django.shortcuts import render
from .forms import BuscarProductoForm
from .models import Producto

def index(request):
    form = BuscarProductoForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        categoria = form.cleaned_data.get('categoria')

        # Filtrar productos según los parámetros de búsqueda
        productos = Producto.objects.filter(
            nombre__icontains=nombre,
            categoria__icontains=categoria
            # Puedes agregar más condiciones según tus necesidades de búsqueda
        )

    else:
        # Si no se ha enviado el formulario, mostrar todos los productos
        productos = Producto.objects.all()

    return render(request, 'producto/index.html', {'form': form, 'productos': productos})


def todos_los_productos(request):
    productos = Producto.objects.all()

    return render(request, 'producto/todos_los_productos.html', {'productos': productos})
