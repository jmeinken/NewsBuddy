# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170610_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsfeed',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
