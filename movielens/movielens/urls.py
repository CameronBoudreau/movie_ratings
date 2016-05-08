from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^ratings/', include('ratings.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
]
