from django import forms


class ContactEntryForm(forms.Form):
    name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Full Name'})
    )
    email = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Email', 'type': 'email'})
    )
    subject = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Subject'})
    )
    message = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'placeholder': 'Message', 'rows': 5})
    )


class SubscriberForm(forms.Form):
    name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Full Name'})
    )
    email = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Email', 'type': 'email'})
    )
    country = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Country'})
    )
