from django import forms
from .models import Series, Review

class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ['title']

class SeriesReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']
