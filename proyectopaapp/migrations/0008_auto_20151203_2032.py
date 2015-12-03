# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectopaapp', '0007_auto_20151203_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='lineaDeProduccion',
        ),
        migrations.AddField(
            model_name='producto',
            name='lineaDeProduccion',
            field=models.ForeignKey(default=1, to='proyectopaapp.LineaDeProduccion'),
            preserve_default=False,
        ),
    ]
