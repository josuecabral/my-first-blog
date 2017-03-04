# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0004_auto_20170303_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrado',
            name='fecha_nacimiento',
            field=models.DateTimeField(),
        ),
    ]
