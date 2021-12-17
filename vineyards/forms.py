from django import forms
from .models import ReviewAndRating, Vineyard, VineyardUser


class ReviewRatingForm(forms.ModelForm):
    class Meta:
        model = ReviewAndRating
        fields = [
            'recommended', 'value', 'service', 'cleanliness', 'location',
            'sustainability', 'title', 'review'
        ]


class VineyardForm(forms.ModelForm):
    class Meta:
        model = Vineyard
        fields = [
            "name", "text", "wine_rg", "wines", "size", "grapes",
            "owner", "visits", "region", "regions", "cover"
        ]


class VineyardUserForm(forms.ModelForm):
    class Meta:
        model = VineyardUser
        fields = ["email2", "address", "website", "number"]
