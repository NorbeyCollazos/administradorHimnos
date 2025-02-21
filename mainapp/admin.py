from django.contrib import admin
from .models import Himnosycoros, Notas, Tipos, Categorias

# Register your models here.
class HimnosycorosAdmin(admin.ModelAdmin):

    search_fields = ('titulo', 'himno', 'autor') #para crear fitro de busqueda
    list_display = ('titulo', 'autor') #para mstrar columnas
    list_filter = ('categoria','estado', 'nota', "autor", "tipo") #para filtrar

class NotasAdmin(admin.ModelAdmin):

    search_fields = ('id_nota','nota') #para crear fitro de busqueda
    list_display = ('id_nota','nota') #para mstrar columnas

class TiposAdmin(admin.ModelAdmin):

    search_fields = ('id_tipo','tipo') #para crear fitro de busqueda
    list_display = ('id_tipo','tipo') #para mstrar columnas

class CategoriasAdmin(admin.ModelAdmin):

    search_fields = ('id_categoria','categoria') #para crear fitro de busqueda
    list_display = ('id_categoria','categoria') #para mstrar columnas


admin.site.register(Himnosycoros, HimnosycorosAdmin)
admin.site.register(Notas, NotasAdmin)
admin.site.register(Tipos, TiposAdmin)
admin.site.register(Categorias, CategoriasAdmin)