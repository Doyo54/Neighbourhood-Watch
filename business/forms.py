from django import forms
from django.contrib.auth.models import User


class AddBussinessForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Business Name','class': 'form-control mb-4'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Business Description','class': 'form-control mb-4','rows': 5,}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Business Email','class': 'form-control mb-4'}))
    neighbourhood = forms.ChoiceField(required=True, widget=forms.Select(attrs={'placeholder': 'Neighbourhood','class': 'form-control mb-4'}))

    def __init__(self, *args, **kwargs):
        super(AddBussinessForm, self).__init__(*args, **kwargs)
        self.fields['neighbourhood'].choices = [(e.id, e.title) for e in NeighbourHood.objects.all()]

class AddPostForm(forms.Form):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Post Title'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control mb-4', 'rows': 5, 'placeholder':'Description'}))
    category = forms.ChoiceField(choices=CATEGORIES, required=True, widget=forms.Select(attrs={'class': 'form-control mb-4', 'placeholder':'Select Category'}))
    neighbourhood = forms.ChoiceField(label=u'Select Your Neighbourhood', required=True, widget=forms.Select(attrs={'class': 'form-control mb-4'}))

    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)
        self.fields['neighbourhood'].choices = [(e.id, e.title) for e in NeighbourHood.objects.all()]