# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Businesses'
