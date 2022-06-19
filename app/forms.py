from django import forms
from django.contrib.auth.models import User
from .models import Neighbourhood,Profile

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ('user',)

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile_picture', 'location', 'bio','neighbourhood']