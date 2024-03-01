from django import forms

class CrForm(forms.Form):
    name=forms.CharField()
    heroic_name=forms.CharField()
