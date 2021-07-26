from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.utils.html import mark_safe


# Create your models here.


class Category(models.Model):
    cat_name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.cat_name



CHOICE_STAR = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

CHOICE_SIZE = (
    ('XXL', 'XXL'),
    ('XL', 'XL'),
    ('L', 'L'),
)

CHOICE_COLOR = (
    ('red', 'red'),
    ('black', 'black'),
    ('gray', 'gray'),
    ('yellow', 'yellow'),
)


class Product(models.Model):
    pro_cat_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    pro_name = models.CharField(max_length=100)
    pro_price = models.BigIntegerField()
    pro_offer_price = models.BigIntegerField(default=0)
    pro_fake_price = models.BigIntegerField(null=True, blank=True)
    pro_image = models.FileField(blank=True)
    pro_description = models.TextField(null=True, blank=True)
    pro_star = models.CharField(max_length=10, choices=CHOICE_STAR, null=True, blank=True)
    pro_availability = models.BooleanField(default=True)

    def __str__(self):
        return self.pro_name


class PostImage(models.Model):
    post = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')


class Product_Size(models.Model):
    size_key = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    product_Size = models.CharField(max_length=50, choices=CHOICE_SIZE, default=CHOICE_SIZE[2])

    def __str__(self):
        return self.product_Size


class Product_Color(models.Model):
    color_key = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    product_Color = models.CharField(max_length=50, choices=CHOICE_COLOR, default=CHOICE_COLOR[2])

    def __str__(self):
        return self.product_Color


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
    cart_color = models.CharField(max_length=50,null=True)
    cart_size = models.CharField(max_length=50,null=True)
    cart_date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.cart_product.pro_name

    @property
    def cart_pro_price(self):
        return self.cart_quantity * self.cart_product.pro_price

    @property
    def cart_offer_price(self):
        return self.cart_product.pro_offer_price * self.cart_quantity

    @property
    def subtotal(self):
        return (self.cart_quantity * self.cart_product.pro_price) - (self.cart_product.pro_offer_price * self.cart_quantity)


CHOICE = (
    ('one', 'one'),
    ('two', 'two'),
)


class Edemo(models.Model):
    demo_choice = models.CharField(max_length=20, choices=CHOICE, default=1)

    def __str__(self):
        return self.demo_choice
