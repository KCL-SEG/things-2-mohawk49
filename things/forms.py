"""Forms of the project."""
from django import forms
from .models import Thing


class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']

    name = forms.CharField(max_length=35)
    description = forms.CharField(
        max_length=120,
        widget=forms.Textarea
    )
    quantity = forms.NumberInput(attrs={'min': 0, 'max': 50})
