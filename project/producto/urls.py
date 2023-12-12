from django.urls import path
from . import views

app_name = "producto"

urlpatterns = [
    path('', views.index, name="index"),
    path('todos/', views.todos_los_productos, name='todos_los_productos'),
]
