# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 19:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='daily_ration',
            new_name='daily_ratio',
        ),
    ]
