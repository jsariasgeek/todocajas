from django.contrib import admin

from clientes.models import Cliente


# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cedula_o_nit', 'telefono', 'correo', 'direccion', 'ciudad')
    autocomplete_fields = ['ciudad']


admin.site.register(Cliente, ClienteAdmin)