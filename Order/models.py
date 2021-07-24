from django.db import models
from django.contrib.auth.models import User
from Product.models import Product


# Create your models here.

class Checkout(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_name", null=True,
                             blank=True)
    product = models.CharField(max_length=40, null=True)
    ammount = models.CharField(max_length=40)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)


class Order_History(models.Model):
    history_user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="history_user_name", null=True,
                             blank=True)
    ord_product = models.CharField(max_length=20,null=True)
    ord_size = models.CharField(max_length=20)
    ord_color = models.CharField(max_length=20)
    ord_quantity = models.CharField(max_length=20)
    ord_date = models.DateTimeField(auto_now_add=True)
    ord_status = models.BooleanField(default=False)
    ord_payment_id = models.CharField(max_length=100,null=True,blank=True)