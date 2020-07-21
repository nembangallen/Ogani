from django.contrib import admin
from .models import Category, Product, ProductImage


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'image', 'category_photo')
    list_display = ('name', 'category_photo')
    readonly_fields = ('category_photo',)


admin.site.register(Category, CategoryAdmin)


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 3
    readonly_fields = ('product_image',)


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('name', 'category', 'product_photo', 'new_price',
                    'featured', 'created_by')
    readonly_fields = ('product_photo',)
    list_filter = ['created_at']


admin.site.register(Product, ProductAdmin)
