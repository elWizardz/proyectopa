# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectopaapp', '0005_lineadeproduccion_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineadeproduccion',
            name='procesos',
            field=models.ManyToManyField(to='proyectopaapp.Proceso'),
        ),
    ]
