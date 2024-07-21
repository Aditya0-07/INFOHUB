from django import forms
from movies.models import Review
from movies.models import Movie

class movieform(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']
