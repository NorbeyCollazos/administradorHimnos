from django.contrib import admin
from .models import Himno, Alabanza, HimnosFeAlabanza

# Register your models here.

class HimnoAdmin(admin.ModelAdmin):

    search_fields = ('titulo', 'himno', 'autor') #para crear fitro de busqueda
    list_display = ('titulo', 'autor') #para mstrar columnas
    list_filter = ('estado', 'nota', "autor", "tipo") #para filtrar


class AlabanzaAdmin(admin.ModelAdmin):

    search_fields = ('titulo', 'himno', 'autor') #para crear fitro de busqueda
    list_display = ('titulo', 'autor') #para mstrar columnas
    list_filter = ('estado', 'nota', "autor", "tipo") #para filtrar


class HimnosFeAlabanzaAdmin(admin.ModelAdmin):

    search_fields = ('titulo', 'himno', 'autor') #para crear fitro de busqueda
    list_display = ('titulo', 'autor') #para mstrar columnas
    list_filter = ('estado', 'nota', "autor", "tipo") #para filtrar


admin.site.register(Himno, HimnoAdmin)
admin.site.register(Alabanza, AlabanzaAdmin)
admin.site.register(HimnosFeAlabanza, HimnosFeAlabanzaAdmin)

