from django.db import models

# Create your models here.
class HimnosHimnarioCristiano(models.Model):
    numero = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150, verbose_name="Título")
    himno = models.TextField()
    nota = models.CharField(max_length=50, verbose_name="Nota", null=True, blank=True)
    tipos = [
        ('Adoración', 'Adoración'),
        ('Alabanza', 'Alabanza'),
        ('Especiales', 'Especiales'),
        ('Cumpleaños', 'Cumpleaños'),
        ('Himno de Fe y Alabanza', 'Himno de Fe y Alabanza'),
        ('Cantico al Señor', 'Cantico al Señor'),
    ]
    tipo = models.CharField(max_length=50, choices=tipos, default="Adoración", null=True, blank=True)
    number = models.CharField(max_length=5, verbose_name="Número de Himno", null=True, blank=True)
    url = models.CharField(max_length=250, verbose_name="Url", null=True, blank=True)



    class Meta:
        verbose_name = "Himnario Cristiano"
        verbose_name_plural = "Himnario Cristiano"
    

    def __str__(self):
        return self.titulo
