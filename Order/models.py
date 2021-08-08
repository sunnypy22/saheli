from django.db import models
from django.contrib.auth.models import User
from Product.models import Product



CHOICE_ORDER_STATUS = (
    ('Prepare To Dispatch', 'Prepare To Dispatch'),
    ('Dispatch', 'Dispatch'),
    ('Received', 'Received'),
)


# Create your models here.

class Checkout(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_name", null=True,
                             blank=True)
    product = models.CharField(max_length=500, null=True)
    ammount = models.CharField(max_length=200)
    payment_id = models.CharField(max_length=100)
    billing_company = models.CharField(max_length=100,null=True,blank=True)
    billing_postcode = models.CharField(max_length=100,null=True,blank=True)
    order_address = models.CharField(max_length=500,null=True,blank=True)
    billing_phone = models.CharField(max_length=100,null=True,blank=True)
    order_comments = models.CharField(max_length=500,null=True,blank=True)
    paid = models.BooleanField(default=False)
    order_status = models.CharField(max_length=50, choices=CHOICE_ORDER_STATUS, null=True, blank=True, default=CHOICE_ORDER_STATUS[0])
    ord_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id

class Order_History(models.Model):
    history_user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="history_user_name", null=True,
                                          blank=True)
    order_checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE, related_name="History_Checkout", null=True,
                                       blank=True)
    ord_product = models.CharField(max_length=500, null=True)
    ord_size = models.CharField(max_length=20)
    ord_color = models.CharField(max_length=20)
    ord_quantity = models.CharField(max_length=20)
    ord_payment_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.ord_payment_id