# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-22 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='u_mob',
            field=models.CharField(max_length=15),
        ),
    ]