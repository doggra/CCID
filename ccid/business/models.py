# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField()
    link = models.CharField(max_length=254, default="#")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Businesses'


class WaitingAds(models.Model):
    image = models.ImageField(help_text='Size: 600px x 100px')


class ResultsAds(models.Model):
    image = models.ImageField(help_text='Size: 600px x 200px')


class Fact(models.Model):
    text = models.TextField()

    def __unicode__(self):
        return self.text
