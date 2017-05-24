from django.conf.urls import url
from django.contrib import admin
from ccid.views import Home, CalculateRates, Quote

urlpatterns = [
	url(r'^$', Home.as_view(), name='home'),
	url(r'^calculate/$', CalculateRates.as_view(), name='calculate_rates'),
	url(r'^quote/$', Quote.as_view(), name='quote'),

    url(r'^admin/', admin.site.urls),
]
