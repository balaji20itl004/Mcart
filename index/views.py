from django.shortcuts import render, redirect
from . models import *
from django.core.mail import send_mail


# Create your views here.

def category_products():
    return category.objects.all()
    


def index(request):
    categories = category_products()
    b=product.objects.filter(trending_product=False)
    mobiles_category = category.objects.get(name="Mobiles")
    apple_mobiles = product.objects.filter(category=mobiles_category, product_vendor="Apple Store")
    laptop_category=category.objects.get(name="Laptops and PCs")
    laptops = product.objects.filter(category=laptop_category, trending_product=False)

    query = request.GET.get('product_name',"").strip() 
    search= product.objects.filter(product_name__icontains=query) if query else product.objects.none()

    index={

    "categories":categories, 
    "product":b,  
    "products":apple_mobiles,
    "laptop":laptops,
    "search":search,
    "query":query

    }

    return render(request,"home/homes.html", index)



def products_page(request, id): 
   categories=category_products()
   category_name = category.objects.get(id=id)
   
   brands = product.objects.filter(category=category_name).values('brands').distinct()
   print(brands)
   brand_products = {}
   for brand in brands:
        brand_name = brand['brands']
        brand_products[brand_name] = product.objects.filter(category=category_name, brands=brand_name)
        
   products_page={
    "brand_products": brand_products, 
    "category":categories,
    "category_name":category_name
    }
   
   return render(request, "home/products.html", products_page)

def search_product(request):
    query = request.GET.get('product_name',"").strip()
    search = product.objects.filter(product_name__icontains = query) if query else product.objects.none()

    return render(request, "home/products.html", {"search":search, "query":query})


def contactus(request):
    products=category_products()
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        comment=request.POST.get('comment')

        send_mail(
            subject=f"Message from {name} ({email})",
            message=comment,
            from_email=email,
            recipient_list=['balajiexplorer2023@gmail.com'],
        )
        return redirect('contactus')
    
    return render(request, "home/contactus.html",{"product":products})
