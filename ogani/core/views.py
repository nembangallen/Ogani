from django.shortcuts import render
from products.models import Category, Product


def home_view(request):
    categories = Category.objects.all()
    featured_products = Product.objects.filter(featured=True)
    template_name = 'home.html'
    context = {
        'categories': categories,
        'featured_products': featured_products
    }
    return render(request, template_name, context)
