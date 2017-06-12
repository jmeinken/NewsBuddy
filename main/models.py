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
    created_on = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_on', '-article_date', '-article_time']
    
    def __unicode__(self):
        return self.title
    
