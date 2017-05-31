# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Business, WaitingAds, ResultsAds, Fact

admin.site.register(Business)
admin.site.register(WaitingAds)
admin.site.register(ResultsAds)
admin.site.register(Fact)
