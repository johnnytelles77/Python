from django.urls import path

from . import views

app_name = "cliente"

urlpatterns = [
    path("", views.home, name="index"),
    path("crear_clientes_varios/", views.crear_clientes_varios,),
    path("busqueda/", views.busqueda,name="busqueda"),
    path("crear/", views.crear, name="form"),
]