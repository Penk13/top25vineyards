from django import forms


class ReviewRatingForm(forms.Form):
    recommended = forms.IntegerField()
    value = forms.IntegerField()
    service = forms.IntegerField()
    cleanliness = forms.IntegerField()
    location = forms.IntegerField()
    sustainability = forms.IntegerField()
    review = forms.CharField(
        label="Review",
        widget=forms.Textarea(
            attrs={'placeholder': 'Write your personal review here ... (minimum 50 characters)', 'rows': 5})
    )

    def clean_recommended(self):
        cleaned_data = self.cleaned_data
        recommended = cleaned_data.get('recommended')
        if recommended < 1 or recommended > 20:
            raise forms.ValidationError("Please enter a number between 1-20")
        return recommended

    def clean_value(self):
        cleaned_data = self.cleaned_data
        value = cleaned_data.get('value')
        if value < 1 or value > 20:
            raise forms.ValidationError("Please enter a number between 1-20")
        return value

    def clean_service(self):
        cleaned_data = self.cleaned_data
        service = cleaned_data.get('service')
        if service < 1 or service > 20:
            raise forms.ValidationError("Please enter a number between 1-20")
        return service

    def clean_cleanliness(self):
        cleaned_data = self.cleaned_data
        cleanliness = cleaned_data.get('cleanliness')
        if cleanliness < 1 or cleanliness > 20:
            raise forms.ValidationError("Please enter a number between 1-20")
        return cleanliness

    def clean_location(self):
        cleaned_data = self.cleaned_data
        location = cleaned_data.get('location')
        if location < 1 or location > 20:
            raise forms.ValidationError("Please enter a number between 1-20")
        return location

    def clean_sustainability(self):
        cleaned_data = self.cleaned_data
        sustainability = cleaned_data.get('sustainability')
        if sustainability < 1 or sustainability > 20:
            raise forms.ValidationError("Please enter a number between 1-20")
        return sustainability

    def clean_review(self):
        cleaned_data = self.cleaned_data
        review = cleaned_data.get('review')
        if len(review) <= 50:
            raise forms.ValidationError("Please enter a minimum of 50 char")
        return review
