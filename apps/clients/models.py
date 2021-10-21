
from django.db import models
from apps.products.models import Producto

# Create your models here.
class Cliente (models.Model):
    nombre= models.CharField(max_length=50,verbose_name="nombre")
    fecha = models.DateField(verbose_name="fecha")
    cedula= models.IntegerField(verbose_name="cedula")
    casado= models.BooleanField(verbose_name="casado")
    producto= models.ManyToManyField (Producto,through='ClienteProducto')

    
    def __str__(Self):
        return Self.nombre
    
    class Meta:
        verbose_name = "cliente"
        verbose_name_plural ="clientes"

class ClienteProducto(models.Model):
    producto =models.ForeignKey(Producto,on_delete=models.CASCADE,verbose_name="producto")
    cliente =models.ForeignKey(Cliente,on_delete=models.CASCADE,verbose_name="cliente")
    total =models.DecimalField(max_digits=10,decimal_places=2,verbose_name="total")
    



