from django.db import models
from django.conf import settings
from shop.models import Product


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_MODEL_USER, on_delete=models.CASCADE)
    products = models.ManyToManyField('CartItem')
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.user.user_name


class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_MODEL_USER, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
