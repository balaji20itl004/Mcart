from vendorsignup import views
from django.urls import path

urlpatterns =[
    path("sellproducts", views.sellproducts, name="sellproducts"),
]