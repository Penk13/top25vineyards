from django import forms
from .models import ReviewAndRating


class ReviewRatingForm(forms.ModelForm):
    class Meta:
        model = ReviewAndRating
        fields = ['recommended', 'value', 'service',
                  'cleanliness', 'location', 'sustainability', 'title', 'review']
