# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-22 12:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_manager', '0005_auto_20181122_1220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_device',
            old_name='d_id',
            new_name='d',
        ),
        migrations.RenameField(
            model_name='user_device',
            old_name='u_id',
            new_name='u',
        ),
    ]
