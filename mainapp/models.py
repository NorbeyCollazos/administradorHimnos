from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Notas(models.Model):
    id_nota = models.AutoField(primary_key=True)
    nota = models.CharField(max_length=50, verbose_name="Nota")

    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Notas"
    
    def __str__(self):
        return self.nota


class Tipos(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50, verbose_name="Tipo")

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
    
    def __str__(self):
        return self.tipo

class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=100, verbose_name="Categoria")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return self.categoria



class Himnosycoros(models.Model):
    id_himno = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150, verbose_name="Título")
    categorias = [
        ('Adoracion', 'Adoracion'),
        ('Alabanza', 'Alabanza'),
        ('Himnos', 'Himnos'),
    ]
    categoria = models.CharField(max_length=25, choices=categorias, default="Adoracion")
    tonos = [
        ('mayor', 'Mayor'),
        ('menor', 'Menor')
    ]
    tono = models.CharField(max_length=10, choices=tonos, default="mayor")
    notas = [
        ('C', 'C'),
        ('Cm', 'Cm'),
        ('D', 'D'),
        ('Dm', 'Dm'),
        ('E', 'E'),
        ('Em', 'Em'),
        ('F', 'F'),
        ('Fm', 'Fm'),
        ('G', 'G'),
        ('Gm', 'Gm'),
        ('A', 'A'),
        ('Am', 'Am'),
        ('B', 'B'),
        ('Bm', 'Bm'),
    ]
    nota = models.CharField(max_length=10, choices=notas, default="C")
    tipos = [
        ('Alabanza', 'Alabanza'),
        ('Misioneros', 'Misioneros'),
        ('Evangelisticos', 'Evangelisticos'),
    ]
    tipo = models.CharField(max_length=25, choices=tipos, default="Alabanza")
    autor = models.CharField(max_length=50, verbose_name="Autor", null=True, blank=True)
    himno = models.TextField()
    url = models.CharField(max_length=150, verbose_name="Url", null=True, blank=True)
    estados = [
        ('nuevo', 'nuevo'),
        ('', ''),
    ]
    estado = models.CharField(max_length=50, verbose_name="Estado", choices=estados, default="nuevo", null=True, blank=True)
    numerotono = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Himno y Coro"
        verbose_name_plural = "Himnos y Coros"
    

    def __str__(self):
        return self.titulo










