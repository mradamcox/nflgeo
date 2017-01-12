# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nflmap', '0009_auto_20161218_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='nfl_name',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='college',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]