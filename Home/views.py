from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from Product.models import Category, Product, Product_Color,CHOICE_COLOR,CHOICE_SIZE


# Create your views here.


def index(request):
    data = Product.objects.all().order_by('-id')[0:4]
    high_data = Product.objects.filter(pro_star = 5)[0:3]
    return render(request, 'index.html',{'data':data,'high_data':high_data})


from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string


def demo(request):
    cat = Category.objects.all()
    data = Product.objects.all()

    return render(request, 'demo.html', {'cat': cat, 'data': data})




def product_list(request):
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
    return render(request, 'product_list.html',{'cat': cat, 'data': pro, 'color': color})







def filter_data(request):
    color_choice = CHOICE_COLOR[0:]
    pro = Product.objects.all()
    return render(request,'demo.html',{'color':color_choice,'data':pro})

@csrf_exempt
def try_ajax(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        # post = Product_Color.objects.filter(product_Color = post_id)
        post = Product_Color.objects.filter(product_Color = post_id)
        color_key = []
        for i in post:
            color_key.append(i.id)
        pro = Product.objects.filter(id__in = color_key).distinct()
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


def contact_us(request):
    return render(request, 'contact_us.html')


def faqs(request):
    return render(request, 'faqs.html')


def order_tracking(request):
    return render(request, 'order_tracking.html')


# def demo(request):
#     data = Demo.objects.all()
#     return render(request, 'demo.html', {'data': data})
#
#
# @csrf_exempt
# def demo1(request):
#     if request.method == 'POST':
#         post_id = request.POST.get('post_id')
#         post = Demo.objects.get(pk=post_id)
#         print(post_id)
#         filter_pro = New_One.objects.filter(fdn__id=post_id)
#         print(filter_pro)
#         j_docs = serializers.serialize('json', [post], ensure_ascii=False)
#
#         # t = render_to_string('demo.html', {'value': post})
#         # print(t)
#         return JsonResponse({'j_docs': j_docs})
#     else:
#         return JsonResponse({'j_docs': 'sunny'})