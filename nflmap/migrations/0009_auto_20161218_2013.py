# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nflmap', '0008_auto_20161204_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='id',
        ),
        migrations.AlterField(
            model_name='player',
            name='nfl_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
