from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Wishlist, Cart, Product_Size, Product_Color
from django.contrib import messages


# Create your views here.

def shop(request):
    cat = Category.objects.all()
    pro = Product.objects.all()
    return render(request, 'category-grid.html', {'cat': cat, 'data': pro})


def cat_filter(request, pid):
    pro = Product.objects.get(id=pid)
    cat = Category.objects.all()
    return render(request, 'cat_filter.html', {'cat': cat, 'data': pro})


def product_description(request, pid):
    pro = Product.objects.get(id=pid)
    size = Product_Size.objects.filter(size_key_id=pid)
    color = Product_Color.objects.filter(color_key_id=pid)
    check_cart = Cart.objects.filter(cart_product_id=pid)
    if check_cart:
        start = 1
    else:
        start = 0
    if request.method == "POST":
        if "wishlist_form" in request.POST:

            if Wishlist.objects.filter(wish_list_product=pro.id).exists():
                messages.warning(request, 'Product {} already exists in wishlist!'.format(pro.pro_name))
            else:
                data = Wishlist.objects.create(wish_list_product_id=pro.id, wish_list_user=request.user,
                                               wish_list_status=True)
                data.save()
                return redirect("wishlist")
        elif "cart_form" in request.POST:
            if start == 1:
                data = Cart.objects.get(cart_product_id=pid)
                data.cart_quantity += int(request.POST.get("quantity"))
                final_price = pro.pro_price - pro.pro_offer_price
                data.cart_price = data.cart_quantity * final_price
                data.cart_color = request.POST.get('product_color')
                data.cart_size = request.POST.get('product_size')

                data.save()
                return redirect("cart")
            else:
                quantity = int(request.POST.get("quantity"))
                final_price = pro.pro_price - pro.pro_offer_price
                price = quantity * final_price
                cart_color = request.POST.get('product_color')
                cart_size = request.POST.get('product_size')
                data = Cart(cart_user=request.user, cart_product_id=pro.id, cart_status=True, cart_quantity=quantity,
                            cart_price=price,cart_color=cart_color,cart_size=cart_size)
                data.save()
                return redirect("cart")
    else:
        pass
    return render(request, 'product_description.html', {'pro': pro,'size':size,'color':color})


def wishlist(request):
    data = Wishlist.objects.filter(wish_list_user=request.user)
    return render(request, 'wishlist.html', {'data': data})


def del_wishlist(request, pid):
    data = Wishlist.objects.get(id=pid)
    data.delete()
    return redirect("shop")


@login_required
def cart(request):
    data = Cart.objects.filter(cart_user=request.user)
    user_id = str(request.user.id)
    cart = Cart.objects.raw(
        'SELECT id,total(cart_price) as total FROM Product_cart WHERE cart_user_id="' + user_id + '"')
    return render(request, 'cart.html', {'data': data, 'cart': cart})


def update_cart(request, pid):
    try:
        data = Cart.objects.get(id=pid)
        pro_id = data.cart_product.id
        size = Product_Size.objects.filter(size_key_id = pro_id)
        color = Product_Color.objects.filter(color_key_id=pro_id)
        if request.method == "POST":
            quantity = request.POST.get('quantity')
            product_id = request.POST.get('product_id')
            cart_color = request.POST.get('product_color')
            cart_size = request.POST.get('product_size')
            final_price = data.cart_product.pro_price - data.cart_product.pro_offer_price
            conv_price = int(quantity) * final_price
            price = str(conv_price)
            user = str(request.user.id)
            update_cart = Cart.objects.raw(
                'UPDATE Product_cart SET cart_quantity= "' + quantity + '", cart_price= "' + price + '", cart_color= "' + cart_color + '", cart_size= "' + cart_size + '" WHERE cart_product_id = "' + product_id + '" AND cart_user_id="' + user + '" ')
            return render(request, 'cart.html', {'data': update_cart})
        else:
            pass
        return render(request, 'cart_product_desc.html', {'pro': data,'size':size,'color':color})
    except TypeError:
        return redirect("cart")


def del_cart(request, pid):
    data = Cart.objects.get(id=pid)
    data.delete()
    return redirect("cart")


def checkout(request):
    return render(request, 'checkout.html')
