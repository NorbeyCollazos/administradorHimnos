# Generated by Django 5.1.5 on 2025-02-21 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_categorias_alter_himnosycoros_categoria'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Alabanza',
        ),
        migrations.DeleteModel(
            name='Himno',
        ),
        migrations.DeleteModel(
            name='HimnosFeAlabanza',
        ),
    ]
