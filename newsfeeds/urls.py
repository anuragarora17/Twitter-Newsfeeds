from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
                       url(r'^$', views.CountryFormView.as_view(), name='index'),

                       )