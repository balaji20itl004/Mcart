from django import forms
from index.models import *

class categoryform(forms.ModelForm):
    class Meta:
        model = product
        fields = ['category','product_name','product_vendor','product_image','brands','product_quantity','original_price','new_price','product_description']