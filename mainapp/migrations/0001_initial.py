# Generated by Django 3.0.8 on 2021-03-05 20:21

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Himno',
            fields=[
                ('numero', models.IntegerField(auto_created=True, max_length=10, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150, verbose_name='Título')),
                ('tono', models.CharField(choices=[('mayor', 'Mayor'), ('menor', 'Menor')], default='mayor', max_length=10)),
                ('nota', models.CharField(choices=[('C', 'C'), ('Cm', 'Cm'), ('D', 'D'), ('Dm', 'Dm'), ('E', 'E'), ('Em', 'Em'), ('F', 'F'), ('Fm', 'Fm'), ('G', 'G'), ('Gm', 'Gm'), ('A', 'A'), ('Am', 'Am'), ('B', 'B'), ('Bm', 'Bm')], default='C', max_length=10)),
                ('tipo', models.CharField(default='Adoracion', max_length=25)),
                ('autor', models.CharField(max_length=50, verbose_name='Autor')),
                ('himno', ckeditor.fields.RichTextField(verbose_name='Himno')),
                ('url', models.CharField(max_length=150, verbose_name='Url')),
                ('estado', models.CharField(default='nuevo', max_length=50, verbose_name='Estado')),
                ('numerotono', models.IntegerField(default=0, max_length=5)),
            ],
            options={
                'verbose_name': 'Himno',
                'verbose_name_plural': 'Himnos',
            },
        ),
    ]
