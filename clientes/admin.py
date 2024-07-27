from django.contrib import admin

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cedula_o_nit', 'telefono', 'correo', 'direccion', 'ciudad')


admin.site.register(Cliente, ClienteAdmin)