from django.db import models

from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Paises'

class Departamento(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre


class Ciudad(models.Model):
    nombre = models.CharField(max_length=60)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre + ' - ' + self.departamento.nombre
    
    def get_queryset(self):
        return Ciudad.objects.sort_by('nombre')

    class Meta:
        verbose_name_plural = 'Ciudades'