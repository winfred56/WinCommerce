from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('CartItem')
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField()

    def __str__(self):
    	return self.user.username



class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


    def __str__(self):
    	return f"{self.quantity} of {self.product.name}"
