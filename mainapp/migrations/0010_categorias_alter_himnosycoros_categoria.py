# Generated by Django 5.1.5 on 2025-02-20 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_alter_alabanza_numerotono_alter_himno_numerotono_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=100, verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.AlterField(
            model_name='himnosycoros',
            name='categoria',
            field=models.CharField(choices=[('Adoracion', 'Adoracion'), ('Alabanza', 'Alabanza'), ('Himnos', 'Himnos')], default='Adoracion', max_length=25),
        ),
    ]
