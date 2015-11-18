# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('proyectopaapp', '0004_auto_20151104_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineaDeProduccion',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('capacidad', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999)])),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('tiempoDeEntrada', models.DateTimeField()),
            ],
        ),
    ]
