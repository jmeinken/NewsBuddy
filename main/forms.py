from django import forms

from . import models

class NewsFeedForm(forms.ModelForm):
    class Meta:
        model = models.NewsFeed
        fields = '__all__'   # or fields = '__all__'