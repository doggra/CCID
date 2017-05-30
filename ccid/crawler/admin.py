# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Crop, Quarter, Meridian, Deductible, CrawlerRequest, CrawlerResult


admin.site.register(Crop)
admin.site.register(Quarter)
admin.site.register(Meridian)
admin.site.register(Deductible)
admin.site.register(CrawlerRequest)
admin.site.register(CrawlerResult)