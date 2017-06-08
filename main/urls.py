from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^ajax/get_rss', views.ajax_get_rss, name='ajax_get_rss'),
#     url(r'^new_newsfeed', views.new_newsfeed, name='new_newsfeed'),
]