from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from ccid.views import Home, CalculateRates, Quote, About


urlpatterns = [

	url(r'^$', Home.as_view(), name='home'),
	url(r'^about/$', About.as_view(), name='about'),
	url(r'^calculate/$', CalculateRates.as_view(), name='calculate_rates'),
	url(r'^quote/(?P<sec>[a-zA-Z0-9-]+)/$', Quote.as_view(), name='quote'),
    url(r'^admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)