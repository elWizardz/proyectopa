# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectopaapp', '0009_auto_20151206_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='state',
        ),
        migrations.AddField(
            model_name='instancia',
            name='terminado',
            field=models.BooleanField(default=False),
        ),
    ]
