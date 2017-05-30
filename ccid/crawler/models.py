# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import uuid
from django.db import models
from business.models import Business


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
    datetime = models.DateTimeField(auto_now_add=True)
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

    def __unicode__(self):
        return self.datetime.strftime("%Y/%m/%d %H:%M")


class CrawlerResult(models.Model):
    request = models.ForeignKey(CrawlerRequest, null=True)
    business = models.ForeignKey(Business, null=True)
    liability = models.CharField(max_length=50, default=0)
    premium = models.CharField(max_length=30, default=0)