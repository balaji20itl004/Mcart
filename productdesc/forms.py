from .models import *
from django import forms


class commentform(forms.ModelForm):
    class Meta:
        model = comments
        fields =['text','review_image']
        widgets = {
            'text' : forms.Textarea(attrs={
                'placeholder': 'enter your comments'
            })
        }