from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Himno(models.Model):
    numero = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150, verbose_name="Título")
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
        ('Adoracion', 'Adoracion'),
        ('Misioneros', 'Misioneros'),
        ('Evangelisticos', 'Evangelisticos'),
    ]
    tipo = models.CharField(max_length=25, choices=tipos, default="Adoracion")
    autor = models.CharField(max_length=50, verbose_name="Autor", null=True, blank=True)
    himno = models.TextField()
    url = models.CharField(max_length=150, verbose_name="Url", null=True, blank=True)
    estados = [
        ('nuevo', 'nuevo'),
        ('', ''),
    ]
    estado = models.CharField(max_length=50, verbose_name="Estado", choices=estados, default="nuevo", null=True, blank=True)
    numerotono = models.IntegerField(max_length=5, default=0)


    class Meta:
        verbose_name = "Himno de Adoración"
        verbose_name_plural = "Himnos de Adoración"
    

    def __str__(self):
        return self.titulo



class Alabanza(models.Model):
    numero = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150, verbose_name="Título")
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
    numerotono = models.IntegerField(max_length=5, default=0)


    class Meta:
        verbose_name = "Coro de Alabanza"
        verbose_name_plural = "Coros de Alabanza"
    

    def __str__(self):
        return self.titulo




class HimnosFeAlabanza(models.Model):
    numero = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150, verbose_name="Título")
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
        ('Congregacional', 'Congregacional'),
        ('Misioneros', 'Misioneros'),
        ('Evangelisticos', 'Evangelisticos'),
    ]
    tipo = models.CharField(max_length=25, choices=tipos, default="Congregacional")
    autor = models.CharField(max_length=50, verbose_name="Autor", null=True, blank=True)
    himno = models.TextField()
    url = models.CharField(max_length=150, verbose_name="Url", null=True, blank=True)
    estados = [
        ('nuevo', 'nuevo'),
        ('', ''),
    ]
    estado = models.CharField(max_length=50, verbose_name="Estado", choices=estados, default="nuevo", null=True, blank=True)
    numerotono = models.IntegerField(max_length=5, default=0)


    class Meta:
        verbose_name = "Himno de Fé y Alabanza"
        verbose_name_plural = "Himnos de Fé y Alabanza"
    

    def __str__(self):
        return self.titulo










