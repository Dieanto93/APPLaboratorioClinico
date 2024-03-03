from django.contrib import admin
from .models import Paciente, Administrativo, Tecnico, Examen_disponible

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'edad', 'direccion')
    search_fields = ['cedula']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class Examen_disponibleAdmin(admin.ModelAdmin):
    list_display = ('nombre_examen', 'unidad', 'area')
    search_fields = ['area']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Administrativo)
admin.site.register(Tecnico)
admin.site.register(Examen_disponible, Examen_disponibleAdmin)