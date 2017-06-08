from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^ajax/get_rss', views.ajax_get_rss, name='ajax_get_rss'),
    url(r'^newsfeed/new', views.new_newsfeed, name='new_newsfeed'),
    url(r'^newsfeed/edit/(?P<newsfeed_id>[0-9]+)', views.edit_newsfeed, name='edit_newsfeed'),
    url(r'^newsfeed', views.newsfeed, name='newsfeed'),
]