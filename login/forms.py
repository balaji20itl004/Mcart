from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class customregisterfrom(UserCreationForm):
    username=forms.CharField(max_length=10, required=True)
    email=forms.EmailField(required=True)
    password1=forms.CharField(widget=forms.PasswordInput(),label="password")
    password2=forms.CharField(widget=forms.PasswordInput(), label="confirm password")

    class Meta:
        model=User
        fields=['username','email','password1','password2']

    def cleaned_data(self):
        email=self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("this email is already exists")
        return email


class userprofileform(forms.ModelForm):
    class Meta:
        model = userprofile
        fields = ['profile','dob','address','city','pincode','mobile_no']

        widgets={
            'profile':forms.FileInput(attrs={'class':'custom-file-upload'}),
            'dob':forms.DateInput(attrs={'placeholder':'YYYY-MM-DD'}),
            'mobile_no':forms.NumberInput(attrs={'readonly':'readonly'})
        }