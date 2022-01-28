from django.contrib import admin
from .models import Product, Category, A_image, A_color, A_size


admin.site.register(A_image)
admin.site.register(A_color)
admin.site.register(A_size)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display        = ['name', 'description', 'slug', 'seller', 'brand', 'discount_price', 'price', 'display_image','in_stock']
    editable_fields     = ['discount_price', 'price', 'in_stock', 'description']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display        = ['product', 'category', 'slug']
    prepopulated_fields = {'slug': ('category',)}


