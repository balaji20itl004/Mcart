from django.urls import path
from . import views


urlpatterns = [
    path("payment_page/<int:pid>/", views.payment_page, name="payment_page"),
    path("cart_payment_page", views.cart_payment, name="cart_payment_page"),
    path("payment_confirm/cash_on_delivary/<int:id>/",views.cash_on_delivary, name="cash_on_delivary_single"),
    path("payment_confirm/cash_on_delivary/",views.cash_on_delivary, name="cash_on_delivary"),
    path("payment_confirm/upi/<int:id>/",views.upi, name="upisingle"),
    path("payment_confirm/upi/",views.upi, name="upicart"),
    path("payment_confirm/card/<int:id>/",views.card, name="cardsingle"),
    path("payment_confirm/card/",views.card, name="card"),
    



]