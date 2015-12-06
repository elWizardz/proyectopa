# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectopaapp', '0008_auto_20151203_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instancia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lista_pendientes', models.TextField(null=True)),
                ('proceso', models.ForeignKey(to='proyectopaapp.Proceso')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='state',
            field=models.CharField(max_length=50, default='Procesando'),
        ),
        migrations.AddField(
            model_name='instancia',
            name='producto',
            field=models.ForeignKey(to='proyectopaapp.Producto'),
        ),
    ]
