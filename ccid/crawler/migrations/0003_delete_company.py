# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 09:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0002_company'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Company',
        ),
    ]
