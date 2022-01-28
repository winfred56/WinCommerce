# Generated by Django 3.1.4 on 2022-01-28 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('brand', models.CharField(max_length=100)),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('display_image', models.ImageField(upload_to='display_images/')),
                ('slug', models.SlugField(max_length=355, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('in_stock', models.BooleanField(default=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Grocery', 'Grocery'), ('Phones & Tablets', 'Phones & Tablets'), ('Health & Beauty', 'Health & Beauty'), ('Home & Office', 'Home & Office'), ('Electronics', 'Electronics'), ('Computing', 'Computing'), ('Fashion', 'Fashion'), ('Sports & Sporting Goods', 'Sports & Sporting Goods'), ('Baby Products', 'Baby & Products'), ('Automobiles', 'Automobile'), ('Books', 'Books'), ('Movies', 'Movies'), ('Music', 'Music'), ('Toys & Games', 'Toys & Games'), ('Garden & Outdoors', 'Garden & Outdoors'), ('Miscellaneous', 'Miscellaneous'), ('Pet Supplies', 'Pet & Supplies'), ('Livestock', 'Livestock'), ('Industrial & Scientific', 'Industrial & Scientific')], max_length=100)),
                ('slug', models.SlugField(max_length=355, unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='A_sizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='A_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='other_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='A_colors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]
