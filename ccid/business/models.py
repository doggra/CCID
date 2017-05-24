# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField()
