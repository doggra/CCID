# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from .forms import LandLocationForm, CropInfoForm
from business.models import Business


class Home(TemplateView):

    template_name = 'ccid/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['land_form'] = LandLocationForm()
        context['crop_form'] = CropInfoForm()
        return context

class CalculateRates(TemplateView):
    """ View for displaying ads before redirecting to results page
    """

    template_name = 'ccid/ads_page.html'

class Quote(TemplateView):

    template_name = 'ccid/quote.html'

    def get_context_data(self, **kwargs):
        context = super(Quote, self).get_context_data(**kwargs)
        context['companies'] = Business.objects.all()
        return context
