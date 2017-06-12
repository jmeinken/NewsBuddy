# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models

# Create your models here.

class NewsFeed(models.Model):
 
    url = models.URLField()
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500, blank=True, null=True)
    publication = models.CharField(max_length=500, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    article_date = models.DateField(max_length=500, blank=True, null=True, default=datetime.date.today)
    article_time = models.TimeField(max_length=500, blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.now)
    published = models.BooleanField(default=True)
    read_time = models.IntegerField(blank=True, null=True)
    
    PRINT = 'print'
    VIDEO = 'video'
    AUDIO = 'audio'
    INTERACTIVE = 'interactive'
    MEDIA_TYPE_CHOICES = (
        (PRINT, 'print'),
        (VIDEO, 'video'),
        (AUDIO, 'audio'),
        (INTERACTIVE, 'interactive'),
    )
    media_type = models.CharField(max_length=60, choices=MEDIA_TYPE_CHOICES, default=PRINT,)
    
    class Meta:
        ordering = ['-created_on', '-article_date', '-article_time']
    
    def __unicode__(self):
        return self.title
    
