from django.urls import path
from . import views

urlpatterns=[
    path("cartpage",views.cartpage, name="cartpage"),
    path("remove_from_cart/<int:cid>",views.remove_from_cart, name="remove_from_cart"),
]