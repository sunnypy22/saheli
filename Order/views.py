from django.shortcuts import render, redirect

from Order.models import Checkout
from Product.models import Cart
import razorpay
from django.views.decorators.csrf import csrf_exempt




def checkout(request):
    data = Cart.objects.filter(cart_user=request.user.id)
    user_id = str(request.user.id)
    cart = Cart.objects.raw(
        'SELECT id,total(cart_price) as total FROM Product_cart WHERE cart_user_id="' + user_id + '"')
    if request.method == 'POST':
        ammount = float(request.POST.get("ammount")) * 100
        product = request.POST.get("product")
        client = razorpay.Client(auth=("rzp_test_l5VpO7rP3PiD3H", "brki2hlaIjeRC78vVdkm0izV"))
        payment = client.order.create({'amount': ammount, 'currency': 'INR', 'payment_capture': '1'})
        coffee = Checkout(name=request.user, product=product, ammount=ammount, payment_id=payment['id'])
        coffee.save()
        return render(request, 'checkout.html', {'payment': payment})
    return render(request, 'checkout.html', {'data': data, 'cart': cart})


@csrf_exempt
def success(request):
    if request.method == 'POST':
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
        user = Checkout.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()
        try:
            if user.paid == True:
                user = str(request.user.id)

                cart = Cart.objects.raw(
                    'DELETE FROM Product_cart WHERE cart_user_id="' + user + '"')
                return render(request, 'success.html', {'cart': cart})
        except TypeError:
            return render(request, 'success.html')
        return render(request, 'success.html')
