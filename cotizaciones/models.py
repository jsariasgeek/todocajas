from django.db import models

class ItemCotizacion(models.Model):
    producto = models.ForeignKey('ordenes_de_produccion.Producto', on_delete=models.CASCADE)
    material = models.ForeignKey('ordenes_de_produccion.Material', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total_item = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.producto.nombre

    class Meta:
        verbose_name_plural = 'Items de Cotizacion'

# Create your models here.
class Cotizacion(models.Model):
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    fecha = models.DateField()
    items = models.ManyToManyField(ItemCotizacion)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    agregar_iva = models.BooleanField()
    iva = models.DecimalField(max_digits=10, decimal_places=2)