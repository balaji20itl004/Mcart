from django.db import models
from index.models import *
from django.contrib.auth.models import User

"""class Payment(models.Model):
    PAYMENT_METHODS = [
        ('COD', 'Cash on Delivery'),
        ('UPI', 'UPI'),
        ('CARD', 'Credit/Debit Card'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE) 
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    upi_id = models.CharField(max_length=50, blank=True, null=True)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    card_expiry = models.CharField(max_length=5, blank=True, null=True) 
    card_cvv = models.CharField(max_length=4, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment by {self.user.username} - {self.payment_method} for {self.product.product_name}"""