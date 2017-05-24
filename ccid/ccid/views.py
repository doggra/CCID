# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from .forms import LandLocationForm, CropInfoForm


class Home(TemplateView):
    template_name = 'ccid/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['land_form'] = LandLocationForm()
        context['crop_form'] = CropInfoForm()
        return context