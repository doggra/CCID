#-*- coding: utf-8 -*-

from django import forms
from crawler.models import Quarter, Meridian, Crop, Deductible


class LandLocationForm(forms.Form):
	quarter = forms.ModelChoiceField(queryset=Quarter.objects.all())
	section = forms.CharField()
	township = forms.CharField()
	_range = forms.CharField()
	meridian = forms.ModelChoiceField(queryset=Meridian.objects.all())
	deductible = forms.ModelChoiceField(queryset=Deductible.objects.all())


class CropInfoForm(forms.Form):
	crop = forms.ModelChoiceField(label='Crop type', queryset=Crop.objects.all())
	acres = forms.IntegerField()
	coverage = forms.DecimalField(label='Coverage ( $ / Acre )')