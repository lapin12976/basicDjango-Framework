from django.shortcuts import render
from mainapp.models import Product, ProductCategory
# Create your views here.

def index(request):
    context = {
        'title': 'GeekShop',
        'header': 'GeekShop Store',
        'button': 'Начать покупки',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'header': 'GeekShop',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
