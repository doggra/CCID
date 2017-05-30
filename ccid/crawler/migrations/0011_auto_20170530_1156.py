# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20170524_1004'),
        ('crawler', '0010_crawlerrequest_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crawlerrequest',
            name='result',
        ),
        migrations.RemoveField(
            model_name='crawlerrequest',
            name='token',
        ),
        migrations.AddField(
            model_name='crawlerresult',
            name='business',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Business'),
        ),
        migrations.AddField(
            model_name='crawlerresult',
            name='liability',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='crawlerresult',
            name='request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crawler.CrawlerRequest'),
        ),
        migrations.AlterField(
            model_name='crawlerresult',
            name='price',
            field=models.CharField(default=0, max_length=30),
        ),
    ]