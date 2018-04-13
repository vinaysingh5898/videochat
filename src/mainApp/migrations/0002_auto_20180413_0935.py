# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='City',
            field=models.CharField(max_length=500, default='', blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Country',
            field=models.CharField(max_length=500, default='', blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='State',
            field=models.CharField(max_length=500, default='', blank=True),
        ),
    ]
