# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 00:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copywriting', '0003_auto_20160423_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='title',
            field=models.TextField(blank=True),
        ),
    ]
