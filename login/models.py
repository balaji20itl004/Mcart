from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userprofile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile=models.ImageField(upload_to='uploads/',null=False, blank=False)
    dob=models.DateField(null=False, blank=False)
    address=models.TextField(null=False, blank=False)
    city = models.CharField(max_length=20, null=False, blank=False)
    pincode=models.IntegerField(default=628501)
    mobile_no = models.BigIntegerField(null=False, blank=False)

    def __str__(self):
        return self.user.username



