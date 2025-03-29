from django.shortcuts import render, redirect
from index.models import *
from login.models import *
from productdesc.models import *
from index.views import category_products
import re
from django.contrib import messages

# Create your views here.
def payment_page(request, pid):
    categories = category_products()
    products = product.objects.get(id = pid)
    user_profile = userprofile.objects.get(user = request.user)

    context = {
    "products":products, 
    "profile":user_profile, 
    "product_category":categories,

    }

    return render(request, "payment_dashboard.html", context)


def cart_payment(request):
    categories = category_products()
    carts= cart.objects.filter(user = request.user)
    
    total_price = 0
    for item in carts:  
        total_price += item.products.new_price

    context = {
    "cart":carts, 
    "cart_payment_page":True,
    "categories":categories,
    "total_price":total_price

    }

    return render(request, "payment_dashboard.html", context)

def cash_on_delivary(request, id=None):

    cod_product = None
    cod_carts = None

    if id:
        cod_product = product.objects.get(id = id)
        totalprice = cod_product.new_price
    else:
            cod_carts = cart.objects.filter(user = request.user)
            totalprice = 0
            for item in cod_carts:  
                totalprice += item.products.new_price

    context = {
            "method": "COD", 
            "products":cod_product, 
            "carts":cod_carts, 
            "totalprice":totalprice
            }
    return render(request, "cod_confirm.html", context)



def upi(request, id=None):
        upi_id = None
        upi_cart = None
        if id:
              upi_id = product.objects.get(id = id)
        else:
              upi_cart = cart.objects.filter(user = request.user)

        if request.method == "POST":
              upi = request.POST.get("UPI")

              if validate(upi):
                    context_upi ={
                          "products": upi_id, 
                          "carts": upi_cart, 
                          "method":"upi"
                    }
                    return render(request, "upi_card_confirm.html", context_upi)
              else:
                    messages.error(request, "invalid upi please enter correct upi")
                    return redirect("upisingle", id=id) if id else redirect("upicart")
              
        context={
                  "method":"upi", 
                  "products":upi_id, 
                  "carts":upi_cart  
              }

        return render(request, "cod_confirm.html",context)



def card(request, id=None):
    id = None
    card_cart = None

    if id:
          id = product.objects.get(id=id)
    else:
          card_cart = cart.objects.filter(user = request.user)

    
    if request.method == "POST":
          cname = request.POST.get("card-name")
          cno = request.POST.get("card-number")
          cvv = request.POST.get("card-cvv")
        
          is_valid, message = validate_card(cname, cno, cvv)

          if not is_valid:
                messages.error(request, message)
                return redirect("card")
          return render(request, "upi_card_confirm.html",{"products":id, "carts":card_cart})

    return render(request, "cod_confirm.html",{"method":"card"})

def validate_card(cname,cno, cvv):
      name_pattern = r"^[a-zA-Z]+$"
      number_pattern = r"^\d{12}$"
      cvv_pattern = r"\d{3}$"

      is_name_valid = re.match(name_pattern, cname)
      is_number_valid = re.match(number_pattern, cno)
      is_cvv_valid = re.match(cvv_pattern, cvv)

      if not is_name_valid:
            return False, "Invalid name. Only letters and spaces are allowed."
      elif not is_number_valid:
            return False, "Please enter a valid 16-digit card number in 'xxxx xxxx xxxx xxxx' format."
      elif not is_cvv_valid:
            return False, "Please enter a valid 3-digit CVV."
      
      return True, "Card details are valid."

def validate(upi):
                upi_handles = [
                "axis", "okaxis",
                "hdfcbank", "okhdfcbank",
                "icici", "okicici",
                "sbi", "oksbi",
                "kotak", "okkotak",
                "pnb", "okpnb",
                "barodapay", "bob",
                "unionbank", "okunion",
                "idfc", "okidfc",
                "indus", "okindus",
                "fbl", "federal",
                "yesbank", "okyes",
                "ybl", "paytm", "apl", "upi"
                ]

                upi_handle_patterns = "|".join(upi_handles)

                pattern = rf"^[a-z0-9A-Z._-]+@({upi_handle_patterns})$"
                return re.match(pattern, upi)