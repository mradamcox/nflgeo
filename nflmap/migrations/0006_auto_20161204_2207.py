# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-05 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nflmap', '0005_auto_20161204_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='nflid',
            field=models.IntegerField(),
        ),
    ]
