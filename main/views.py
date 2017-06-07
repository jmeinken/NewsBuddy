# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urllib2

from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    context = {}
    context['nav'] = 'home'
    return render(request, 'main/home.html', context)

def about(request):
    context = {}
    context['nav'] = 'about'
    return render(request, 'main/about.html', context)

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
