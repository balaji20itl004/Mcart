from django.urls import path
from productdesc import views

urlpatterns=[
    path("product_page/<int:id>/",views.product_page,name="product_page"),
    path("update_comment/<int:id>/",views.update_comment,name="update_comment"),
    path("delete_comment/<int:id>",views.delete_comment,name="delete_comment"),
    path("addtocart", views.add_to_cart, name="addtocart"),
    path("samsung/",views.new_product, name = "samsung"),
    path("a56/",views.samsung_a56, name="samsung_a56")
]