from django.conf.urls import url, include

from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^logout_success/$', views.logout_success, name='logout_success'),
    url(r'^', include('registration.backends.simple.urls'))
]
