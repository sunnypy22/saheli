from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from Product.models import Category, Product, Product_Color, CHOICE_COLOR, CHOICE_SIZE
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.


def index(request):
    data = Product.objects.all().order_by('-id')[0:4]
    high_data = Product.objects.filter(pro_star=5)[0:3]
    return render(request, 'index.html', {'data': data, 'high_data': high_data})


from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string


def demo(request):
    return render(request, 'demo.html')


def filter_data(request):
    color_choice = CHOICE_COLOR[0:]
    pro = Product.objects.all()
    return render(request, 'demo.html', {'color': color_choice, 'data': pro})


@csrf_exempt
def try_ajax(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        # post = Product_Color.objects.filter(product_Color = post_id)
        post = Product_Color.objects.filter(product_Color=post_id)
        color_key = []
        for i in post:
            color_key.append(i.id)
        pro = Product.objects.filter(id__in=color_key).distinct()
        t = render_to_string('demo.html', {'data': pro})

        return JsonResponse({'data': t})
    else:
        return JsonResponse({'j_docs': 'sunny'})


def blog(request):
    return render(request, 'blog.html')


def blog_detail(request):
    return render(request, 'blog_detail.html')


def about(request):
    return render(request, 'about.html')


@login_required
def contact_us(request):
    if request.method == "POST":
        order_comments = request.POST.get('order_comments')
        send_mail('Contact You from {username}'.format(username=request.user.username),
                  order_comments,
                  request.user.email,  # FROM
                  ['sehgalc655@gmail.com'],  # TO
                  fail_silently=False)
        return redirect("index")
    else:
        pass
    return render(request, 'contact_us.html')


def faqs(request):
    return render(request, 'faqs.html')



