from django import forms
from .models import City


class FormCity(forms.ModelForm):
    name = forms.CharField(label='search', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = City
        fields = ['name']

