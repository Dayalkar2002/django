from django import forms
from.models import Dc

class Ddc(forms.ModelForm):
    class Meta:
        model =Dc

        fields=['name','heroic_name']

        labels={'name':'Enter first name'}
    
