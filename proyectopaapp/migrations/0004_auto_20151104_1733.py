# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectopaapp', '0003_auto_20151104_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proceso',
            name='id',
            field=models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True),
        ),
    ]
