from django.shortcuts import render, redirect
from productdesc.models import *

# Create your views here
def cartpage(request):
    cart_products = cart.objects.filter(user = request.user)
    total_price = 0
    for item in cart_products:  
        total_price += item.products.new_price
    
    return render(request, "addtocart.html", {"c_products":cart_products, "total_price":total_price})

def remove_from_cart(request, cid):
    cart_items = cart.objects.get(id = cid)
    cart_items.delete()
    return redirect("cartpage")