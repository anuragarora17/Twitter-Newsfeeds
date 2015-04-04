__author__ = 'animesh'
from django import forms


class CountryForm(forms.Form):
    country = forms.ChoiceField(choices=[('1', 'India'), ('2', 'South Africa'), ('3', 'United Stated of America')])