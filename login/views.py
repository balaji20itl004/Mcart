from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import customregisterfrom
from index.views import category_products
from.forms import *
from index.models import *
from django.contrib.auth import get_user_model
from productdesc.models import *
# Create your views here.


def signup(request):
    if request.method=="POST":
        register_form=customregisterfrom(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
    else:
        register_form=customregisterfrom()
    return render(request,"registration/signup.html" ,{"register_forms":register_form})


def logout_page(request):
    logout(request)
    return redirect('login')



def userdashboard(request):
    categories= category_products()

    if request.user.is_authenticated:
        try:
            userformdisplay = userprofile.objects.get(user=request.user)
            cart_products = cart.objects.filter(user = request.user)
            total_price = 0
            for item in cart_products:  
                total_price += item.products.new_price
            
            context= {
                "userprofiledisplay": userformdisplay, 
                "categories":categories,
                "c_products":cart_products, 
                "total_price":total_price
            }
            return render(request, "user_dashboard.html", context)

        except userprofile.DoesNotExist:
            if request.method == 'POST':
                userform = userprofileform(request.POST, request.FILES)
                if userform.is_valid():
                    userprofiles = userform.save(commit=False)
                    userprofiles.user = request.user 
                    userprofiles.save()
                    return redirect('userdashboard')
            else:
                userform = userprofileform()

            context1= {
                "userprofile": userform,
                "categories":categories
            }
    else:
        return redirect("login")

    return render(request, "user_dashboard.html", context1)



def edit_userprofile(request):
    categories= category_products()
    userformdisplay= userprofile.objects.get(user=request.user)
    userprofileforms= userprofileform(instance = userformdisplay)

    if request.method == 'POST':
        updatedform= userprofileform(request.POST, request.FILES, instance=userformdisplay)
        if updatedform.is_valid():
            updatedform.save()
            return redirect('home')
        
    context= {
            "userprofileforms":userprofileforms, 
            "edit_profile":True, 
            "categories":categories
        }
    return render(request, "user_dashboard.html", context)


User = get_user_model()
print(User)

def deleteprofile(request):
    userprofiledisplay = userprofile.objects.get(user=request.user)
    
    if request.method == "POST":
        User = request.user
        User.delete() 
        return redirect("home")

    return render(request, "delete_confirm.html", {"userprofiledisplay": userprofiledisplay,})
