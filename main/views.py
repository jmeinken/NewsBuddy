# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urllib2

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from . import forms
from . import models


def home(request):
    context = {}
    context['qNewsFeed'] = models.NewsFeed.objects.all()[:30]
    context['nav'] = 'home'
    return render(request, 'main/home.html', context)

def about(request):
    context = {}
    context['nav'] = 'about'
    return render(request, 'main/about.html', context)

# using django form instead for now

# @login_required
# def new_newsfeed(request):
#     context = {}
#     if request.method == 'POST':
#         form = forms.NewsFeedForm(request.POST)
#         if form.is_valid():                            
#             oPage = form.save()
#             return HttpResponse('thanks')
#     else:
#         form = forms.NewsFeedForm()
#     context['form'] = form
#     return render(request, 'main/new_newsfeed.html', context)

def ajax_get_rss(request):
    context = {}
    
    source = request.GET.get('source');

    if source == 'npr':
        url = 'http://www.npr.org/rss/rss.php?id=1001'
    elif source == 'nytimes':
        url = 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
    else:  #CSM
        url = 'http://rss.csmonitor.com/feeds/csm?format=xml'

    response = urllib2.urlopen(url)
    xml = response.read()

    return HttpResponse(xml, content_type='text/xml')
