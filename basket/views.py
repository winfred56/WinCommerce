from django.shortcuts import render
from .models import Cart, CartItem


def add_to_cart(request,slug):
    
