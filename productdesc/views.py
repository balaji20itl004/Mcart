from django.shortcuts import render,  redirect, get_object_or_404
from index.models import *
from .models import *
from .forms import *
import json
from django.http import JsonResponse
from index.views import category_products
# Create your views here.

def product_page(request, id):
    if request.user.is_authenticated:
        products=product.objects.get(id=id)
        related_products = product.objects.filter(category=products.category).exclude(id = products.id).order_by('?')[:4]
        comment=comments.objects.filter(products=products)
        user_already_commented = comment.filter(user=request.user).exists()
        categories = category_products()
    else:
        return redirect("login")
    

    if request.method == 'POST':
        forms=commentform(request.POST, request.FILES)
        if forms.is_valid():
            submitform = forms.save(commit=False)
            submitform.products = products
            submitform.user = request.user
            submitform.save()
            return redirect('product_page', id=id)

    else:
        commentforms = commentform()

    context={
    "product":products, 
    "product_category":categories, 
    "related_products":related_products,
    "commentforms":commentforms,
    "comment":comment,
    "user_already_commented":user_already_commented
    }

    return render(request,"productspage/productspage.html", context)



def new_product(request):
    samsung = product.objects.get(id=32)
    categories=category_products()

    context = {
        "product":samsung,
        "product_category":categories,
        
    }
    return render(request, "productspage/new_products.html", context)


def samsung_a56(request):
    a56 = product.objects.get(id=81)
    categories=category_products()
    return render(request, "productspage/new_products.html", {"a56":a56, "samsung_a56":True,  "product_category":categories,})


def update_comment(request, id):
    categories = category_products()
    products=product.objects.get(id=id)
    comment=comments.objects.filter()
    for i in comment:
        product_id = i.products.id

    products_id = comments.objects.get(products = product_id, user = request.user)
    if request.method == 'POST':
        form = commentform(request.POST,request.FILES, instance=products_id)
        if form.is_valid():
            form.save()
            return redirect('product_page', id = products.id)
    else:
        instance_form = commentform(instance=products_id)
    
    return render(request, "productspage/update_comment.html", {"abc":instance_form, "display_products":products_id, "product_category":categories})        
   

def delete_comment(request, id):
    products = product.objects.get(id = id)
    comment=comments.objects.get(products=products, user=request.user)
    comment.delete()
    return redirect('product_page', id = products.id)
    
    


def add_to_cart(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            product_quantity = (data['productquantity'])
            product_id = (data['pid'])
            
            product_status = get_object_or_404(product, id=product_id)
            if product_status:
                if cart.objects.filter(user = request.user, products_id = product_id ):
                    return JsonResponse({'status': 'already in cart'}, status=200)
                else:
                    if product_status.product_quantity >= product_quantity:
                        cart.objects.create(user = request.user, products_id = product_id, quantity = product_quantity)
                        return JsonResponse({'status': 'added to cart'}, status=200)
                    else:
                        return JsonResponse({'status': 'stock currently not avaliable'}, status=200)

           
        else:
            return JsonResponse({'status': 'login to add cart'}, status = 200)
    else:
        return JsonResponse({'status': 'invalid access'}, status = 400)