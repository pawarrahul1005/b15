# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-23 05:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_manager', '0006_auto_20181122_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='u_perms',
        ),
    ]
