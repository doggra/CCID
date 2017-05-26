# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import uuid
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


class CrawlerRequest(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quarter = models.CharField(max_length=64)
    section = models.CharField(max_length=64)
    township = models.CharField(max_length=64)
    _range = models.CharField(max_length=64)
    meridian = models.CharField(max_length=64)
    crop = models.CharField(max_length=64)
    deductible = models.CharField(max_length=64)
    acres = models.CharField(max_length=64)
    coverage = models.CharField(max_length=64)
    result = models.ForeignKey('CrawlerResult', null=True)

    def __unicode__(self):
        return self.name

    # On save create results

class CrawlerResult(models.Model):
    price = models.CharField(max_length=30)