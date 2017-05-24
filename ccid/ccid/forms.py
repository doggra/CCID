from django import forms
from crawler.models import Quarter, Meridian, CropType


class InsuranceForm(forms.Form):
	quarter = forms.ModelChoiceField(queryset=Quarter.objects.all())
	meridian = forms.ModelChoiceField(queryset=Meridian.objects.all())
	crop_type = forms.ModelChoiceField(queryset=CropType.objects.all())