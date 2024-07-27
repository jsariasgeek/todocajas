from django.db import models

class Cliente(models.Model):
    cedula_o_nit = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    direccion = models.CharField(max_length=200)
    ciudad = models.ForeignKey('ubicaciones.Ciudad', on_delete=models.CASCADE)


