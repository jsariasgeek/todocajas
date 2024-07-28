from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Productos'


class ServicioTodoCaja(models.Model):
    nombre = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_por_unidad_de_medida = models.DecimalField(max_digits=10, decimal_places=2)
    unidad_de_medida = models.CharField(max_length=20)


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Servicios Todo Caja'


class Material(models.Model):
    referencia = models.CharField(max_length=50)
    material = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    peso_en_gr = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    calibre = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    tamaño = models.CharField(max_length=100, null=True)
    unidad_de_venta = models.IntegerField()
    precio_por_pliego = models.DecimalField(max_digits=10, decimal_places=2)
    precio_resma = models.DecimalField(max_digits=10, decimal_places=2)
    precio_resma_sin_iva = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    unidad_de_medida = models.CharField(max_length=20)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)


class Referencia(models.Model):
    referencia = models.CharField(max_length=50)



    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Materiales'