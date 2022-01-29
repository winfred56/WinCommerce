from unicodedata import category
from django.shortcuts import render
from .models import Product, Category

def categories(request):
    return {'categories':Category.objects.all()}

def home(request):
    products = Product.objects.all()
    context  = {'products':products}
    return render(request, 'shop/home.html', context)

def categories_list(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'category':category
    }
    return render(request, 'shop/category.html', context)
