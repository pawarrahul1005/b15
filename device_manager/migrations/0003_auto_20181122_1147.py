# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-22 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_manager', '0002_auto_20181122_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='u_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]