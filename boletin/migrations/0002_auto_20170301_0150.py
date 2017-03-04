# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrado',
            name='apellido',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='registrado',
            name='direccion',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='registrado',
            name='dni',
            field=models.IntegerField(unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='registrado',
            name='nombre',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
