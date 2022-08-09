from django.db import models

# Create your models here.

class Producto(models.Model):
  COMIDA = 1
  POSTRE = 2
  BEBIDA = 3
  ENTRADA = 4

  CATEGORIAS = (
    (COMIDA, "Comida"),
    (POSTRE, "Postre"),
    (BEBIDA, "Bebida"),
    (ENTRADA, "Entrada"),
  )

  nombre = models.TextField()
  categoria = models.IntegerField(choices=CATEGORIAS)
  tipo = models.TextField()
  precio = models.IntegerField()
  disponible = models.BooleanField()
  imagen = models.TextField()
