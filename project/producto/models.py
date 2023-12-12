from django.db import models

class Producto(models.Model):
    # Definición de campos para tu modelo
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)

    # Otros campos...

    def __str__(self):
        return self.nombre
