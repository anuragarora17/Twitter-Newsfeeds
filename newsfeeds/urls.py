from django.conf.urls import patterns, url
from newsfeeds import views


urlpatterns = patterns('',
                       url(r'^$', views.CountryFormView.as_view(), name='index'),
                       url(r'^(?P<country>[^/]+)$', views.CountryNewsView.as_view(), name='news'),
                       )