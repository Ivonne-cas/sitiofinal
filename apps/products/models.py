from django.db import models


# Create your models here.
class Producto (models.Model):
    descripcion= models.CharField(max_length=50,verbose_name="descripcion")
    fecha = models.DateField(verbose_name="fecha")
    cantidad =models.IntegerField(verbose_name="cantidad")
    
    
    def __str__(Self):
        return Self.descripcion
    
    class Meta:
        verbose_name = "producto"
        verbose_name_plural ="productos"
