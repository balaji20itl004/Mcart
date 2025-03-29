from django.db import models
import os
import datetime


def file_name(request,filename):
    now_time= datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_file_name="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_file_name)

# Create your models here.
class category(models.Model):
    name= models.CharField(max_length=150, null=False, blank=False)
    image=models.ImageField(upload_to=file_name, null=True, blank=True)
    description=models.TextField(max_length=500, null=False, blank=False)
    status=models.BooleanField(default=False, help_text="0-SHOW 1-HIDE")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class product(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    product_name= models.CharField(max_length=1500, null=False, blank=False)
    product_vendor= models.CharField(max_length=150, null=False, blank=False)
    product_image=models.ImageField(upload_to=file_name, null=True, blank=True)
    brand_choice=[
        ('Apple','Apple'),
        ('Vivo','Vivo'),
        ('Redmi','Redmi'),
        ('Oppo','Oppo'),
        ('Samsung','Samsung'),
        ('Oneplus','Oneplus'),
        ('Lenovo','Lenovo'),
        ('Dell','Dell'),
        ('LG','LG'),
        ('Acer','Acer'),
        ('Poco','Poco'),
        ('HP','HP'),
        ('Sony','Sony'),
        ('Xbox','Xbox'),
    ]
    brands=models.CharField(max_length=50, choices=brand_choice, null=True, blank=True)
    product_quantity=models.IntegerField(null=False, blank=False)
    original_price=models.IntegerField(null=False, blank=False)
    new_price=models.IntegerField(null=False, blank=False)
    product_description=models.TextField(max_length=5000, null=False, blank=False)
    status=models.BooleanField(default=False, help_text="0-SHOW 1-HIDE")
    trending_product= models.BooleanField(default=False, help_text="0-YES 1-NO")
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product_name