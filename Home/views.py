from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Product.models import Category, Product, Product_Color


# Create your views here.


def index(request):
    return render(request, 'index.html')


from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string


def demo(request):
    cat = Category.objects.all()
    data = Product.objects.all()

    return render(request, 'demo.html', {'cat': cat, 'data': data})


def filter_data(request):
    cat = request.GET.getlist('cat[]')
    all_products = Product.objects.all().order_by('-id').distinct()
    if len(cat) > 0:
        all_products = all_products.filter(pro_cat_name__id__in=cat).distinct()
    t = render_to_string('demo.html', {'data': all_products})
    return JsonResponse({'data': t})


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

@csrf_exempt
def try_ajax(request):
    cat = request.GET.getlist('cat[]')
    size = request.GET.getlist('cat[]')
    colors = request.GET.getlist('cat[]')
    all_products = Product.objects.all().order_by('-id').distinct()
    if len(cat) > 0:
        all_products = all_products.filter(pro_cat_name__id__in=cat).distinct()
    t = render_to_string('demo.html', {'data': all_products})
    return JsonResponse({'data': t})


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
