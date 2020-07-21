from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to='category/', blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def category_photo(self):
        return mark_safe('<img src={} width="100" />'.format(self.image.url))
    category_photo.short_description = 'Image'
    category_photo.allow_tags = True

    def __str__(self):
        return self.name


class Product(models.Model):
    KILOGRAMS = 'kg'
    GRAMS = 'gm'
    LITRE = 'ltr'
    MILILITRE = 'ml'

    METRIC_UNIT_CHOICES = [
        (KILOGRAMS, 'Kilograms'),
        (GRAMS, 'Grams'),
        (LITRE, 'Litre'),
        (MILILITRE, 'Mililitre'),
    ]
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(max_length=2000, null=False)
    featured_image = models.ImageField(upload_to='product/', blank=True)
    metric_unit = models.CharField(
        max_length=3, choices=METRIC_UNIT_CHOICES, default=KILOGRAMS)
    unit = models.IntegerField(default=1)
    old_price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    new_price = models.DecimalField(max_digits=6, decimal_places=2)
    featured = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='products')
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='+')

    def product_photo(self):
        return mark_safe('<img src={} width="100" />'.format(self.featured_image.url))
    product_photo.short_description = 'Featured Image Preview'
    product_photo.allow_tags = True

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_images')
    images = models.ImageField(blank=True, upload_to='product/')

    def product_image(self):
        return mark_safe('<img src={} width="100" />'.format(self.images.url))
    product_image.short_description = 'Image Preview'
    product_image.allow_tags = True

    def __str__(self):
        return self.product.name
