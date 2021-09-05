from Product.models import Cart, Wishlist


def cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(cart_user=request.user).count()
        return {'check_cart': cart}
    else:
        cart = 0
        return {'cart': cart}


def wishlist(request):
    if request.user.is_authenticated:
        data = Wishlist.objects.filter(wish_list_user=request.user).count()
        return {'check_wish': data}
    else:
        data = 0
        return {'check_wish': data}
