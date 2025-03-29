from django.shortcuts import render,redirect
from .forms import *
from .models import *
from index.views import category_products


def sellproducts(request):
    categories = category_products()
    if request.method == 'POST':
        product_form = categoryform(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('home')
  
    products_form = categoryform()

    context={
        "form":products_form,
        "categories":categories
    }

    return render(request, "productupload.html",context)
