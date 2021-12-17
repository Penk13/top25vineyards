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
    def __init__(self, *args, **kw):
        super(VineyardForm, self).__init__(*args, **kw)
        placeholder_text = """
Add here a description and all information about vineyard:
- History
- Estate
- Terroir
- Winemaker and team
- Wines
- etc...
"""
        self.fields['text'].widget.attrs['placeholder'] = placeholder_text
        self.fields['text'].widget.attrs['cols'] = 54
        self.fields['region'].widget.attrs['class'] = "w-75"
        self.fields['regions'].widget.attrs['class'] = "w-75"

    class Meta:
        model = Vineyard
        fields = [
            "name", "text", "wine_rg", "wines", "size", "grapes",
            "owner", "visits", "region", "regions", "cover"
        ]
        labels = {
            "name": "Vineyard or Property Name",
            "text": "Vineyard Description and Information",
            "wine_rg": "Wine Region and Country",
            "wines": "Wines",
            "size": "Size",
            "grapes": "Grapes",
            "owner": "Owner",
            "visits": "Visits",
            "region": "Region",
            "regions": "Regions",
            "cover": "Cover"
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name of your vineyard...", "class": "w-75"}),
            "wine_rg": forms.TextInput(attrs={"placeholder": "Where is your vineyard located: region and country...", "class": "w-75"}),
            "wines": forms.TextInput(attrs={"placeholder": "Wines", "class": "w-75"}),
            "size": forms.TextInput(attrs={"placeholder": "Vineyard Size", "class": "w-75"}),
            "grapes": forms.TextInput(attrs={"placeholder": "Grapes", "class": "w-75"}),
            "owner": forms.TextInput(attrs={"placeholder": "Owner Name", "class": "w-75"}),
            "visits": forms.TextInput(attrs={"placeholder": "Visits", "class": "w-75"}),
        }


class VineyardUserForm(forms.ModelForm):
    class Meta:
        model = VineyardUser
        fields = ["email2", "address", "website", "number"]
        labels = {
            "email2": "Email",
            "address": "Address",
            "website": "Website",
            "number": "Number",
        }
        widgets = {
            "email2": forms.EmailInput(attrs={"placeholder": "Email", "class": "w-75"}),
            "address": forms.TextInput(attrs={"placeholder": "Address", "class": "w-75"}),
            "website": forms.TextInput(attrs={"placeholder": "Website", "class": "w-75"}),
            "number": forms.TextInput(attrs={"placeholder": "Phone Number", "class": "w-75"}),
        }
