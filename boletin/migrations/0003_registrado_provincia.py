# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0002_auto_20170301_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrado',
            name='provincia',
            field=models.CharField(max_length=120, null=True, choices=[('Cordoba', 'Cordoba'), ('La Rioja', 'LaR ioja'), ('Misiones', 'Misiones')]),
        ),
    ]
