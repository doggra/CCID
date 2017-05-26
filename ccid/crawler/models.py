# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models


class Crop(models.Model):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Quarter(models.Model):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Meridian(models.Model):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Deductible(models.Model):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name
