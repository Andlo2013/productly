from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre=models.CharField(max_length=255)
    stock=models.IntegerField()
    puntaje=models.FloatField()
    #onDelete
    #1.- CASCADE: Borra todos los productos de la categoria
    #2.- PROTECT: No se puede borrar la categoria
    #3.- RESTRICT: No se puede borrar la categoria si tiene productos
    #4.- SET_NULL: Pone en null categoriaId si se borra la categoria
    #5.- SET_DEFAULT: Pone un valor por defecto en categoriaId si se borra la categoria
    
    categoria=models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
        )
    creado_en=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre    