# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0003_registrado_provincia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrado',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='registrado',
            name='provincia',
            field=models.CharField(max_length=120, null=True, choices=[('Cordoba', 'Cordoba'), ('La Rioja', 'La Rioja'), ('Misiones', 'Misiones')]),
        ),
    ]
