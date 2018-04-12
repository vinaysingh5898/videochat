# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('PriPhone', models.DecimalField(decimal_places=False, max_digits=10)),
                ('LandMark', models.CharField(blank=True, max_length=500, null=True)),
                ('City', models.CharField(max_length=500, default='')),
                ('State', models.CharField(max_length=500, default='')),
                ('Country', models.CharField(max_length=500, default='')),
                ('PinCode', models.DecimalField(decimal_places=False, max_digits=6)),
                ('AddressLine', models.CharField(blank=True, max_length=500, null=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
