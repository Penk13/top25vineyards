from django import forms
from .models import ReviewAndRating, Vineyard, VineyardUser, Comment
from captcha.fields import CaptchaField
from django.core.files.images import get_image_dimensions


class ReviewRatingForm(forms.ModelForm):
    captcha = CaptchaField()
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
        self.fields['text'].widget.attrs['class'] = "bg-light"
        self.fields['text'].widget.attrs['required'] = True

        self.fields['region'].widget.attrs['class'] = "w-75"
        self.fields['region'].widget.attrs['required'] = True

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
            "wines": "Wines Produced",
            "size": "Vineyard Size",
            "grapes": "Grapes",
            "owner": "Winemaker",
            "visits": "Visits",
            "region": "Region",
            "regions": "Regions",
            "cover": "Upload Main Photo (min. width 900px)"
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name of your vineyard...", "class": "w-75 bg-light", "required": True}),
            "wine_rg": forms.TextInput(attrs={"placeholder": "Where is your vineyard located: region and country...", "class": "w-75 bg-light", "required": True}),
            "wines": forms.TextInput(attrs={"placeholder": "Your most famous and iconic wines...", "class": "w-75 bg-light", "required": True}),
            "size": forms.TextInput(attrs={"placeholder": "Size of your vineyard, if multiple lots, give total area...", "class": "w-75 bg-light", "required": True}),
            "grapes": forms.TextInput(attrs={"placeholder": "Grapes", "class": "w-75 bg-light", "required": True}),
            "owner": forms.TextInput(attrs={"placeholder": "Name of Winemaker, Owner, Vigneron, or...", "class": "w-75 bg-light", "required": True}),
            "visits": forms.TextInput(attrs={"placeholder": "Visiting hours or visit options and conditions...", "class": "w-75 bg-light", "required": True}),
        }

    def clean_cover(self):
        cover = self.cleaned_data.get("cover")
        if not cover:
            raise forms.ValidationError("No image!")
        else:
            w, h = get_image_dimensions(cover)
            if w < 900:
                raise forms.ValidationError("The image is %i pixel wide. Minimum image width is 900px" % w)
            # if h < 900:
            #     raise forms.ValidationError("The image is %i pixel high. Minimum image height is 900px" % h)
        return cover    


class VineyardUserForm(forms.ModelForm):
    def __init__(self, *args, **kw):
        super(VineyardUserForm, self).__init__(*args, **kw)
        self.fields['website'].initial = "https://"
        placeholder_address = "Address"

        self.fields['address'].widget.attrs['placeholder'] = placeholder_address
        self.fields['address'].widget.attrs['cols'] = 54
        self.fields['address'].widget.attrs['rows'] = 5
        self.fields['address'].widget.attrs['class'] = "bg-light"

    captcha = CaptchaField()
    class Meta:
        model = VineyardUser
        fields = ["email2", "address", "website", "web_text", "number"]
        labels = {
            "email2": "Email",
            "address": "Address",
            "website": "Website",
            "web_text": "Website Name",
            "number": "Number",
        }
        widgets = {
            "email2": forms.EmailInput(attrs={"placeholder": "Email", "class": "w-75 bg-light", "required": True}),
            "web_text": forms.TextInput(attrs={"placeholder": "Website Name", "class": "w-75 bg-light", "required": True}),
            "website": forms.TextInput(attrs={"placeholder": "Website", "class": "w-75 bg-light", "required": True}),
            "number": forms.TextInput(attrs={"placeholder": "Phone Number", "class": "w-75 bg-light", "required": True}),
        }


class CommentForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Comment
        fields = [
            'title', 'body'
        ]