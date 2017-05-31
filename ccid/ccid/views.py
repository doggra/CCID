# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import LandLocationForm, CropInfoForm
from .tasks import get_dropdowns
from business.models import Business, WaitingAds, ResultsAds, Fact
from crawler.models import Crop, Quarter, Deductible, Meridian, CrawlerRequest, CrawlerResult
from ccid.tasks import make_request_to_ehailca

class Home(TemplateView):

    template_name = 'ccid/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['land_form'] = LandLocationForm()
        context['crop_form'] = CropInfoForm()
        return context


class About(TemplateView):
    template_name = 'ccid/about.html'


class CalculateRates(TemplateView):
    """ View for displaying ads before redirecting to results page
    """

    template_name = 'ccid/ads_page.html'

    def get_context_data(self, **kwargs):
        context = super(CalculateRates, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):

        township = request.POST.get('township')
        _range = request.POST.get('_range')
        meridian = Meridian.objects.get(pk=request.POST.get('meridian'))
        crop = Crop.objects.get(pk=request.POST.get('crop'))
        deductible = Deductible.objects.get(pk=request.POST.get('deductible'))
        quarter = Quarter.objects.get(pk=request.POST.get('quarter', ''))

        cr = CrawlerRequest.objects.create(quarter=quarter.value,
                                           section=request.POST.get('section', ''),
                                           township=request.POST.get('township', ''),
                                           _range=request.POST.get('_range', ''),
                                           meridian=meridian.value,
                                           crop=crop.value,
                                           deductible=deductible.value,
                                           acres=request.POST.get('acres', ''),
                                           coverage=request.POST.get('coverage', ''))

        make_request_to_ehailca(cr)
        context = {}
        context['sec'] = cr.uuid
        context['ads'] = WaitingAds.objects.all()
        context['fact'] = random.choice(Fact.objects.all())

        return render(request, self.template_name, context)


class Quote(TemplateView):

    template_name = 'ccid/quote.html'

    def get_context_data(self, **kwargs):
        context = super(Quote, self).get_context_data(**kwargs)
        context['results'] = CrawlerResult.objects.filter(request__uuid=self.kwargs['sec']).order_by('premium')
        context['ads'] = ResultsAds.objects.all()
        return context
