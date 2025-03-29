from django.db import models
from index.models import *
from django.contrib.auth.models import User 

# Create your models here.
class comments(models.Model):
    products=models.ForeignKey(product,on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text= models.TextField()
    review_image=models.ImageField(upload_to="uploads/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.products.product_name}"
    

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.products.product_name} ({self.quantity}) - {self.user.username}"
    
    @property
    def total_unit_cost(self):
        return self.products.new_price * self.quantity