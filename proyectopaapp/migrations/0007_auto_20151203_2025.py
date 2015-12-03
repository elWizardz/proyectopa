# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('proyectopaapp', '0006_proceso_capacidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineadeproduccion',
            name='capacidad',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='tiempoDeEntrada',
        ),
        migrations.AddField(
            model_name='lineadeproduccion',
            name='procesos',
            field=models.ManyToManyField(to='proyectopaapp.Proceso'),
        ),
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.PositiveIntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='lineaDeProduccion',
            field=models.ManyToManyField(to='proyectopaapp.LineaDeProduccion'),
        ),
    ]
