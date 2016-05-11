from django.conf.urls import url, include
from . import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

app_name = 'accounts'

urlpatterns = [

    # url(r'^register/',
        # CreateView.as_view(template_name='registration/register.html',
                        #    form_class=UserCreationForm,
                        #    success_url='/'),
        # name='register'),
    # url(r'^$', include('django.contrib.auth.urls')),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^logout_success/$', views.logout_success, name='logout_success'),
    url(r'^register/$', views.register, name='register'),
    url(r'^', include('registration.backends.simple.urls')),
    ]
