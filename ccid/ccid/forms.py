#-*- coding: utf-8 -*-

from django import forms
from crawler.models import Quarter, Meridian, CropType


class LandLocationForm(forms.Form):
	quarter = forms.ModelChoiceField(queryset=Quarter.objects.all())
	section = forms.CharField()
	township = forms.CharField()
	range = forms.CharField()
	meridian = forms.ModelChoiceField(queryset=Meridian.objects.all())

class CropInfoForm(forms.Form):
	crop_type = forms.ModelChoiceField(queryset=CropType.objects.all())
	acres = forms.IntegerField()
	coverage = forms.DecimalField(label='Coverage ( $ / Acre )')