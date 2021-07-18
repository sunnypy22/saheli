from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Checkout(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_name", null=True,
                             blank=True)
    product = models.CharField(max_length=40,null=True)
    ammount = models.CharField(max_length=40)
    payment_id = models.CharField(max_length=40)
    paid = models.BooleanField(default=False)
