from django.core.management.base import BaseCommand
import json

from ubicaciones.models import Ciudad, Departamento, Pais


class Command(BaseCommand):
    help = 'Carga las ubicaciones de la base de datos'


    def handle(self, *args, **options):
        pais = Pais.objects.create(nombre='Colombia')
        # Carga de ubicaciones
        # abre el archivo colombia.json
        with open('ubicaciones/fixtures/colombia.json', 'r') as file:
            data = json.load(file)
            for departamento in data:
                d = Departamento.objects.create(nombre=departamento['departamento'], pais=pais)
                ciudades = [Ciudad.objects.bulk_create([Ciudad(nombre=ciudad, departamento=d) for ciudad in departamento['ciudades']])]

        self.stdout.write(self.style.SUCCESS('Ubicaciones cargadas exitosamente'))