from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Product.models import Category, Product


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
    data = Product.objects.all()

    return render(request, 'product_list.html', {'cat': cat, 'data': data})

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
