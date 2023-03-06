from django.contrib import admin

from .models import Empleado, habilidades
# Register your models here.
admin.site.register(habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )

    def full_name (self,obj):
        #toda la operacione que necesitamos
        #print(obj)
        return obj.first_name + ' ' + obj.last_name
    #
    search_fields = (
        'first_name',
        'last_name',
    )

    list_filter = ('job', 'habilidades')
    #
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)
