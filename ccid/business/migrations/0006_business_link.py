# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0005_auto_20170530_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='link',
            field=models.CharField(default='#', max_length=254),
        ),
    ]
