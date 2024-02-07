from django.contrib.auth.models import User
from django import forms

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User  # Import User from django.contrib.auth.models
        fields = ['username', 'email', 'password']
from django import forms

class ProductSelectionForm(forms.Form):
    product_list = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-control'}))
