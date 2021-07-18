from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.utils.html import mark_safe


# Create your models here.


class Category(models.Model):
    cat_name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.cat_name


class Color(models.Model):
    color_code = models.CharField(max_length=100)

    def __str__(self):
        return self.color_code

class Size(models.Model):
    title = models.CharField(max_length=100)


CHOICE_STAR = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

CHOICE_COLOR = (
    ('Red','Red'),
    ('White','White'),
    ('Black','Black'),
    ('Brown','Brown'),
    ('Gray','Gray'),
)


class Product(models.Model):
    pro_cat_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    pro_name = models.CharField(max_length=100)
    pro_price = models.BigIntegerField()
    pro_offer_price = models.BigIntegerField(default=0)
    pro_fake_price = models.BigIntegerField(null=True, blank=True)
    pro_size = models.ForeignKey(Size, on_delete=models.CASCADE)
    pro_color = models.ForeignKey(Color, on_delete=models.CASCADE,null=True)
    pro_image = models.FileField(blank=True)
    pro_description = models.TextField(null=True, blank=True)
    pro_star = models.CharField(max_length=10, choices=CHOICE_STAR, null=True, blank=True)
    pro_availability = models.BooleanField(default=True)

    def __str__(self):
        return self.pro_name


class PostImage(models.Model):
    post = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')


class Wishlist(models.Model):
    wish_list_user = models.ForeignKey(User, on_delete=models.CASCADE)
    wish_list_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    wish_list_status = models.BooleanField(default=False)


class Cart(models.Model):
    cart_user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_quantity = models.IntegerField(default=1)
    cart_status = models.BooleanField(default=False)
    cart_price = models.IntegerField(blank=True, null=True)
    cart_date = models.DateTimeField(auto_now_add=True)

    @property
    def cart_pro_price(self):
        return self.cart_quantity * self.cart_product.pro_price


CHOICE = (
    ('one', 'one'),
    ('two', 'two'),
)


class Edemo(models.Model):
    demo_choice = models.CharField(max_length=20, choices=CHOICE, default=1)

    def __str__(self):
        return self.demo_choice
