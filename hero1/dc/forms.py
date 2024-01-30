from django import forms

class Ddc(forms.Form):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name=forms.CharField(label='Full Name',choices=GENDER_CHOICES)
    sir_name=forms.CharField(disabled=True)