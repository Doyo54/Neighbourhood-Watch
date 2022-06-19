from django import forms
from django.contrib.auth.models import User
from .models import Neighbourhood

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ('user',)