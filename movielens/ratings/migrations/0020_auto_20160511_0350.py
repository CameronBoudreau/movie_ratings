# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 03:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0019_auto_20160510_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
