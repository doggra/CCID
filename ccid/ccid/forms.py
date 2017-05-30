#-*- coding: utf-8 -*-

from django import forms
from crawler.models import Quarter, Meridian, Crop, Deductible


class LandLocationForm(forms.Form):
    quarter = forms.ModelChoiceField(queryset=Quarter.objects.all())
    section = forms.CharField(max_length=2)
    township = forms.CharField(max_length=2)
    _range = forms.IntegerField(max_value=20, label='Range')
    meridian = forms.ModelChoiceField(queryset=Meridian.objects.all())
    deductible = forms.ModelChoiceField(queryset=Deductible.objects.all())


class CropInfoForm(forms.Form):
    crop = forms.ModelChoiceField(label='Crop type', queryset=Crop.objects.all())
    acres = forms.IntegerField(max_value=999, min_value=1)
    coverage = forms.DecimalField(label='Coverage ( $ / Acre )')
