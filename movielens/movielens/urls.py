from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

app_name = 'home'

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/ratings/', permanent=False),
        name='redirect'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^ratings/', include('ratings.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls'))
]
