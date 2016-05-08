from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

app_name = 'ratings'

urlpatterns = [
    # url(r'^$', views.index, name='index'),

    url(r'^$', RedirectView.as_view(url='/', permanent=False), name='redirect'),

    url(r'^(?P<name>\w+)/$', views.index, name='page'),

    # url(r'^movies/$', views.movie_index, name='movie_index'),

    url(r'^movies/(?P<movie>[0-9]+)$',
        views.movie_detail,
        name='movie_detail'),

    # url(r'^raters/$', views.rater_index, name='rater_index'),

    url(r'^raters/(?P<rater>[0-9]+)$',
        views.rater_detail,
        name='rater_detail'),

    # url(r'^top/$', views.top_detail, name='top'),
]
