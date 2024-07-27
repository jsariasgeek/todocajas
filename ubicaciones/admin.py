from django.contrib import admin

from ubicaciones.models import Ciudad

class CiudadAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Ciudad, CiudadAdmin)