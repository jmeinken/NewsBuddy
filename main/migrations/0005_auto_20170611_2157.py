# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 01:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_newsfeed_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsfeed',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
