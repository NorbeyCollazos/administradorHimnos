from django.contrib import admin
from .models import HimnosHimnarioCristiano

# Register your models here.

class HimnosHimnarioCristianoAdmin(admin.ModelAdmin):

    search_fields = ('titulo', 'himno') #para crear fitro de busqueda
    list_display = ('titulo', 'tipo') #para mstrar columnas
    list_filter = ('tipo',) #para filtrar


admin.site.register(HimnosHimnarioCristiano, HimnosHimnarioCristianoAdmin)
