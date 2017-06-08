# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models




class NewsFeedAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication', 'article_date')
    
admin.site.register(models.NewsFeed, NewsFeedAdmin)
