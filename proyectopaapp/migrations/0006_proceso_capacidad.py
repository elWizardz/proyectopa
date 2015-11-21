# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('proyectopaapp', '0005_lineadeproduccion_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceso',
            name='capacidad',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999)]),
            preserve_default=False,
        ),
    ]
