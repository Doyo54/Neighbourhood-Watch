from django import forms
from django.contrib.auth.models import User
from app.models import Neighbourhood


class AddBussinessForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Business Name','class': 'form-control mb-4'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Business Description','class': 'form-control mb-4','rows': 5,}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Business Email','class': 'form-control mb-4'}))
    neighbourhood = forms.ChoiceField(required=True, widget=forms.Select(attrs={'placeholder': 'Neighbourhood','class': 'form-control mb-4'}))

    def __init__(self, *args, **kwargs):
        super(AddBussinessForm, self).__init__(*args, **kwargs)
        self.fields['neighbourhood'].choices = [(e.id, e.name) for e in Neighbourhood.objects.all()]

