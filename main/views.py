# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urllib2

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from . import forms
from . import models


def home(request):
    context = {}
    context['qNewsFeed'] = models.NewsFeed.objects.filter(published=True)[:30]
    context['nav'] = 'home'
    return render(request, 'main/home.html', context)

def about(request):
    context = {}
    context['nav'] = 'about'
    return render(request, 'main/about.html', context)

@login_required
def newsfeed(request):
    context = {}
    context['qNewsFeed'] = models.NewsFeed.objects.all()
    return render(request, 'main/newsfeed.html', context)

@login_required
def new_newsfeed(request):
    context = {}
    if request.method == 'POST':
        form = forms.NewsFeedForm(request.POST)
        if form.is_valid():                            
            oPage = form.save()
            return redirect('home')
    else:
        form = forms.NewsFeedForm()
    context['form'] = form
    return render(request, 'main/new_newsfeed.html', context)

@login_required
def edit_newsfeed(request, newsfeed_id):
    context = {}
    oNewsFeed = get_object_or_404(models.NewsFeed, pk=newsfeed_id)
    if request.method == 'POST':
        form = forms.NewsFeedForm(request.POST, instance=oNewsFeed)
        if form.is_valid():
            oNewsFeed = form.save()
            return redirect('home')
    else:
        form = forms.NewsFeedForm(instance=oNewsFeed)
    context['form'] = form
    return render(request, 'main/new_newsfeed.html', context)

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
