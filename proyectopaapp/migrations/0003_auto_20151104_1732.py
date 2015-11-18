# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('proyectopaapp', '0002_auto_20151030_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proceso',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='tiempo',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999)]),
        ),
    ]
