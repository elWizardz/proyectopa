# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectopaapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceso',
            name='tiempo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),
        ),
    ]
