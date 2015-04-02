__author__ = 'raghvendra'
from django.conf.urls import patterns, url
from newsfeeds import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       )
