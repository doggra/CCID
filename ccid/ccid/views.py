# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import LandLocationForm, CropInfoForm
from .tasks import get_dropdowns
from business.models import Business
from crawler.models import Crop, Quarter, Deductible, Meridian, CrawlerRequest


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

    def post(self, request, *args, **kwargs):

        township = request.POST.get('township')
        _range = request.POST.get('_range')
        meridian = Meridian.objects.get(pk=request.POST.get('meridian'))
        crop = Crop.objects.get(pk=request.POST.get('crop'))
        deductible = Deductible.objects.get(pk=request.POST.get('deductible'))

        cr = CrawlerRequest.objects.create(quarter=quarter,
                                           section=section,
                                           township=township,
                                           meridian=meridian.value,
                                           crop=crop.value,
                                           deductible=deductible.value,
                                           acres=acres,
                                           coverage=coverage,
                                           _range=_range)


        return render(request, self.template_name)


class Quote(TemplateView):

    template_name = 'ccid/quote.html'

    def get_context_data(self, **kwargs):
        context = super(Quote, self).get_context_data(**kwargs)
        context['companies'] = Business.objects.all()
        return context
