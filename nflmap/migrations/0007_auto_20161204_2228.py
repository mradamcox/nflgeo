# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-05 04:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nflmap', '0006_auto_20161204_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='nflid',
            new_name='nfl_id',
        ),
    ]
