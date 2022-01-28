from itertools import product
from tabnanny import verbose
from unicodedata import category, decimal
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_lenght =100)
    description = models.TextField(blank=True, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    discount_price = models.DecimalField(max_digits=8, decimal_places=2)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    display_image = models.ImageField(upload_to='display_images/')
    slug = models.SlugField(max_length=355, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", kwargs={"slug": self.slug})


    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['-created']


class A_images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='other_images/')

    def __str__(self):
        return f"{self.product.name}'other image"


class A_colors(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product.name}'other color"

class A_sizes(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product.name}'other size"


Grocery= 'Grocery'
Phones_Tablets= 'Phones & Tablets'
Health_Beauty= 'Health & Beauty'
Home_Office= 'Home & Office'
Electronics= 'Electronics'
Computing= 'Computing'
Fashion= 'Fashion'
Sports_Sporting= 'Sports & Sporting Goods'
Baby_Products= 'Baby Products'
Automobile= 'Automobiles'
Books = 'Books'
Movies = 'Movies'
Music= 'Music'
Toys_Games= 'Toys & Games'
Garden_Outdoors= 'Garden & Outdoors'
Miscellaneous= 'Miscellaneous'
Pet_Supplies= 'Pet Supplies'
Livestock= 'Livestock'
Industrial_Scientific = 'Industrial & Scientific'

category_choices = [(Grocery,'Grocery'),(Phones_Tablets,'Phones & Tablets'),(Health_Beauty,'Health & Beauty'),(Home_Office,'Home & Office'),
(Electronics,'Electronics'), (Computing,'Computing'), (Fashion,'Fashion'),(Sports_Sporting,'Sports & Sporting Goods'),
(Baby_Products,'Baby & Products'),(Automobile,'Automobile'),(Books,'Books'),(Movies,'Movies'),(Music,'Music'),(Toys_Games,'Toys & Games'),
(Garden_Outdoors,'Garden & Outdoors'),(Miscellaneous,'Miscellaneous'),(Pet_Supplies,'Pet & Supplies'),(Livestock,'Livestock'),
(Industrial_Scientific,'Industrial & Scientific')
]

class Category(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=category_choices)
    slug = models.SlugField(max_length=355, unique=True)

    def get_absolute_url(self):
        return reverse("shop:categories", kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category