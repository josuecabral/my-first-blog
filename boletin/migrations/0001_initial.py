# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=120, blank=True, null=True)),
                ('dni', models.IntegerField()),
                ('direccion', models.CharField(max_length=120, blank=True, null=True)),
                ('fecha_nacimiento', models.IntegerField()),
                ('iniciado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
