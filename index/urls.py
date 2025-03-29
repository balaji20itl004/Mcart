from django.urls import path
from index import views


urlpatterns = [
    path('home/',views.index,name="home"),
    path('product/<int:id>/',views.products_page,name="product"),
    path('search/',views.search_product,name="search"),
    path('contactus/',views.contactus, name="contactus"),
]