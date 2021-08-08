from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Order.models import Checkout, Order_History
from Product.models import Cart
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.contrib import messages

def checkout(request):
    data = Cart.objects.filter(cart_user=request.user.id)
    user_id = str(request.user.id)
    cart = Cart.objects.raw(
        'SELECT id,total(cart_price) as total FROM Product_cart WHERE cart_user_id="' + user_id + '"')
    if request.method == 'POST':
        ammount = float(request.POST.get("ammount")) * 100
        main_price = float(request.POST.get("ammount"))
        product = request.POST.getlist("product[]")
        ord_size = request.POST.getlist("ord_size[]")
        ord_color = request.POST.getlist("ord_color[]")
        ord_quantity = request.POST.getlist("ord_quantity[]")
        billing_company = request.POST.get("billing_company")
        billing_postcode = request.POST.get("billing_postcode")
        order_address = request.POST.get("order_address")
        billing_phone = request.POST.get("billing_phone")
        order_comments = request.POST.get("order_comments")
        client = razorpay.Client(auth=("rzp_test_l5VpO7rP3PiD3H", "brki2hlaIjeRC78vVdkm0izV"))
        payment = client.order.create({'amount': ammount, 'currency': 'INR', 'payment_capture': '1'})
        coffee = Checkout(name=request.user, product=product, ammount=main_price, payment_id=payment['id'],
                          billing_company=billing_company,
                          billing_postcode=billing_postcode, order_address=order_address, billing_phone=billing_phone,
                          order_comments=order_comments,order_status="Prepare To Dispatch")
        coffee.save()

        ord_payment_id = coffee.payment_id
        for product, ord_size, ord_color, ord_quantity in zip(product, ord_size, ord_color, ord_quantity):
            data = Order_History.objects.create(ord_product=product, ord_size=ord_size, ord_color=ord_color,
                                                ord_quantity=ord_quantity, history_user_name=request.user,
                                                ord_payment_id=ord_payment_id, order_checkout_id=coffee.id)
            data.save()
        details = Cart.objects.filter(cart_user=request.user.id)
        user_id = str(request.user.id)
        cart = Cart.objects.raw(
            'SELECT id,total(cart_price) as total FROM Product_cart WHERE cart_user_id="' + user_id + '"')
        return render(request, 'checkout.html', {'payment': payment, 'details': details, 'pay_cart': cart})
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


@login_required
def order_history(request):
    chckout = Checkout.objects.filter(name=request.user)
    order_history = Order_History.objects.filter(history_user_name=request.user)
    key_a = request.GET.get('sort_by')
    if key_a == "New-To-Old":
        New_To_Old = Checkout.objects.all().order_by('-ord_date')
        return render(request, 'order_history.html', {'chckout': New_To_Old, 'order_history': order_history})
    elif key_a == "Old-To-New":
        Old_To_New = Checkout.objects.all().order_by('ord_date')
        return render(request, 'order_history.html', {'chckout': Old_To_New, 'order_history': order_history})
    elif key_a == "Success-Payment":
        success_checkout = Checkout.objects.filter(name=request.user, paid=True)
        return render(request, 'order_history.html', {'chckout': success_checkout, 'order_history': order_history})
    elif key_a == "Fail-Payment":
        fail_checkout = Checkout.objects.filter(name=request.user, paid=False)
        return render(request, 'order_history.html', {'chckout': fail_checkout, 'order_history': order_history})
    else:
        pass
    return render(request, 'order_history.html', {'chckout': chckout, 'order_history': order_history})


@login_required
def order_tracking(request):
    try:
        if request.method == "POST":
            orderid = request.POST.get('orderid')
            order_email = request.POST.get('order_email')
            data = Checkout.objects.get(payment_id=orderid)
            order_status = data.order_status
            if order_status == "Prepare To Dispatch":
                send_mail('Track Your Order with Best Experiance',
                          'Your Order is {status}'.format(status=order_status),
                          request.user.email,  # FROM
                          [order_email],  # TO
                          fail_silently=False)
                return redirect("order_history")
            elif order_status == "Dispatch":
                send_mail('Track Your Order with Best Experiance',
                          'Your Order is {status}, You will get your order very soon'.format(status=order_status),
                          request.user.email,  # FROM
                          [order_email],  # TO
                          fail_silently=False)
                return redirect("order_history")
            else:
                send_mail('Track Your Order with Best Experiance',
                          'Your Order has been delivered '.format(status=order_status),
                          request.user.email,  # FROM
                          [order_email],  # TO
                          fail_silently=False)
                return redirect("order_history")
        else:
            pass
        return render(request, 'order_tracking.html')
    except:
        messages.error(request,"Please Check With Your Valid Order ID")
        return redirect("order_history")
