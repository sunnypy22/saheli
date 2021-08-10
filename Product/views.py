from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F, Q, When
from .models import Category, Product, Wishlist, Cart, Product_Size, Product_Color, CHOICE_COLOR, CHOICE_SIZE, PostImage
from django.contrib import messages


# Create your views here.

def shop(request):
    cat = Category.objects.all()
    pro = Product.objects.all()
    color = Product_Color.objects.all()
    key_a = request.GET.get('order_by')
    if key_a == "High-To-Low":
        order_by_price_h_to_l = Product.objects.all().order_by('-pro_price')
        return render(request, 'category-grid.html',
                      {'cat': cat, 'data': order_by_price_h_to_l, 'color': color})
    elif key_a == "Low-To-High":
        order_by_price_l_to_h = Product.objects.all().order_by('pro_price')
        return render(request, 'category-grid.html',
                      {'cat': cat, 'data': order_by_price_l_to_h, 'color': color})
    elif key_a == "High-Rating":
        order_by_high_rating = Product.objects.all().order_by('-pro_star')
        return render(request, 'category-grid.html',
                      {'cat': cat, 'data': order_by_high_rating, 'color': color})
    elif key_a == "Low-Rating":
        order_by_low_rating = Product.objects.all().order_by('pro_star')
        return render(request, 'category-grid.html',
                      {'cat': cat, 'data': order_by_low_rating, 'color': color})
    else:
        pass
    return render(request, 'category-grid.html', {'cat': cat, 'data': pro, 'color': color})


def cat_filter(request, pid):
    # pro = Product.objects.get(pro_cat_name=pid)
    pro = Product.objects.all().filter(pro_cat_name_id=pid)
    color_choice = CHOICE_COLOR[0:]
    size_choice = CHOICE_SIZE[0:]
    cat = Category.objects.all()
    color = Product_Color.objects.all()
    key_a = request.GET.get('order_by')
    if key_a == "High-To-Low":
        order_by_price_h_to_l = Product.objects.all().filter(pro_cat_name_id=pid).order_by('-pro_price')
        return render(request, 'cat_filter.html',
                      {'cat': cat, 'data': order_by_price_h_to_l, 'color': color, 'color_choice': color_choice,
                       'size_choice': size_choice})

    elif key_a == "Low-To-High":
        order_by_price_l_to_h = Product.objects.all().filter(pro_cat_name_id=pid).order_by('pro_price')
        return render(request, 'cat_filter.html',
                      {'cat': cat, 'data': order_by_price_l_to_h, 'color': color, 'color_choice': color_choice,
                       'size_choice': size_choice})
    elif key_a == "High-Rating":
        order_by_high_rating = Product.objects.all().filter(pro_cat_name_id=pid).order_by('-pro_star')
        return render(request, 'cat_filter.html',
                      {'cat': cat, 'data': order_by_high_rating, 'color': color, 'color_choice': color_choice,
                       'size_choice': size_choice})
    elif key_a == "Low-Rating":
        order_by_low_rating = Product.objects.all().filter(pro_cat_name_id=pid).order_by('pro_star')
        return render(request, 'cat_filter.html',
                      {'cat': cat, 'data': order_by_low_rating, 'color': color, 'color_choice': color_choice,
                       'size_choice': size_choice})
    else:
        pass
    return render(request, 'cat_filter.html',
                  {'cat': cat, 'data': pro, 'color': color, 'color_choice': color_choice, 'size_choice': size_choice})


@csrf_exempt
def ajax_filter(request):
    color = Product_Color.objects.all()
    color_choice = CHOICE_COLOR[0:]
    size_choice = CHOICE_SIZE[0:]
    cat = Category.objects.all()
    if request.method == 'POST':
        post_id = request.POST.get('post_id')

        request_path = int(request.POST.get('request_path'))
        post = Product_Color.objects.filter(product_Color=post_id)
        size = Product_Size.objects.filter(product_Size=post_id)

        color_key = []
        for i in post:
            color_key.append(i.id)

        size_key = []
        for j in size:
            size_key.append(j.size_key.id)

        if len(post) > 0:

            pro = Product.objects.filter(id__in=color_key, pro_cat_name_id=request_path)
            t = render_to_string('cat_filter.html',
                                 {'cat': cat, 'data': pro, 'color': color, 'color_choice': color_choice,
                                  'size_choice': size_choice})
            return JsonResponse({'data': t})
        elif len(size) > 0:

            pro = Product.objects.filter(id__in=size_key, pro_cat_name_id=request_path)
            t = render_to_string('cat_filter.html',
                                 {'cat': cat, 'data': pro, 'color': color, 'color_choice': color_choice,
                                  'size_choice': size_choice})

            return JsonResponse({'data': t})
        else:
            pass
        pro = Product.objects.all().filter(pro_cat_name_id=request_path)
        t = render_to_string('cat_filter.html', {'cat': cat, 'data': pro, 'color': color, 'color_choice': color_choice,
                                                 'size_choice': size_choice})
        return JsonResponse({'data': t})
    else:
        return JsonResponse({'j_docs': 'sunny'})

def product_description(request, pid):
    pro = Product.objects.get(id=pid)
    cat = Category.objects.all()
    image = PostImage.objects.filter(post_id=pid)
    size = Product_Size.objects.filter(size_key_id=pid)
    color = Product_Color.objects.filter(color_key_id=pid)
    check_cart = Cart.objects.filter(cart_product_id=pid)
    if request.method == "POST":

        if "wishlist_form" in request.POST:

            if Wishlist.objects.filter(wish_list_product=pro.id).exists():
                messages.warning(request, 'Product {} already exists in wishlist!'.format(pro.pro_name))
            else:
                if request.user.is_authenticated:

                    data = Wishlist.objects.create(wish_list_product_id=pro.id, wish_list_user=request.user,
                                               wish_list_status=True)

                    data.save()
                    return redirect("wishlist")
                else:
                    return redirect("signin")
        elif "cart_form" in request.POST:
            if request.user.is_authenticated:
                product_color = request.POST.get('product_color')
                product_size = request.POST.get('product_size')
                check_cart = Cart.objects.filter(cart_user=request.user, cart_product_id=pid, cart_color=product_color,
                                                 cart_size=product_size)
                if check_cart:
                    data = Cart.objects.get(cart_user=request.user, cart_product_id=pid, cart_color=product_color,
                                            cart_size=product_size)
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
                    if len(size) == 0 or len(color) == 0:
                        data = Cart(cart_user=request.user, cart_product_id=pro.id, cart_status=True,
                                    cart_quantity=quantity,
                                    cart_price=price)

                        data.save()
                        return redirect("cart")


                    else:
                        if cart_color == "" or cart_size == "":
                            messages.error(request, 'PLease Choose Your Size And Colour for Better Experience')

                        else:
                            data = Cart(cart_user=request.user, cart_product_id=pro.id, cart_status=True,
                                        cart_quantity=quantity,
                                        cart_price=price, cart_color=cart_color, cart_size=cart_size)

                            data.save()
                            return redirect("cart")
            else:
                return redirect("signin")

    else:
        pass
    return render(request, 'product_description.html', {'pro': pro,'cat':cat, 'size': size, 'color': color, 'image': image})



@login_required
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
        size = Product_Size.objects.filter(size_key_id=pro_id)
        color = Product_Color.objects.filter(color_key_id=pro_id)

        image = PostImage.objects.filter(post_id=pro_id)
        if request.method == "POST":
            quantity = request.POST.get('quantity')
            product_id = request.POST.get('product_id')
            cart_color = request.POST.get('product_color')
            cart_size = request.POST.get('product_size')
            cart_id = request.POST.get('cart_id')

            final_price = data.cart_product.pro_price - data.cart_product.pro_offer_price
            conv_price = int(quantity) * final_price
            price = str(conv_price)
            user = str(request.user.id)
            update_cart = Cart.objects.raw(
                'UPDATE Product_cart SET cart_quantity= "' + quantity + '", cart_price= "' + price + '", cart_color= "' + cart_color + '", cart_size= "' + cart_size + '" WHERE id = "' + cart_id + '" AND cart_user_id="' + user + '" ')
            return render(request, 'cart.html', {'data': update_cart})
        else:
            pass
        return render(request, 'cart_product_desc.html', {'pro': data, 'size': size, 'color': color, 'image': image})
    except TypeError:
        return redirect("cart")


def del_cart(request, pid):
    data = Cart.objects.get(id=pid)
    data.delete()
    return redirect("cart")


def checkout(request):
    return render(request, 'checkout.html')
