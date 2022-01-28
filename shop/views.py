from django.shortcuts import render
from .models import Product, Category

def categories(request):
    return {'categories':Category.objects.all()}

def home(request):
    products = Product.objects.all()
    context  = {'products':products}
    return render(request, 'shop/home.html')
