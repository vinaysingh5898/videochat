# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('PriPhone', models.DecimalField(max_digits=10, decimal_places=False)),
                ('LandMark', models.CharField(null=True, max_length=500, blank=True)),
                ('City', models.CharField(max_length=500, default='')),
                ('State', models.CharField(max_length=500, default='')),
                ('Country', models.CharField(max_length=500, default='')),
                ('PinCode', models.DecimalField(max_digits=6, decimal_places=False)),
                ('AddressLine', models.CharField(null=True, max_length=500, blank=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='user',
        ),
        migrations.DeleteModel(
            name='user_info',
        ),
    ]
