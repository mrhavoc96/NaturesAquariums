from django.db.models import Q      # Q helps us write complex queries with many OR and AND conditions
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Home page - shows all products through pages (paginator)
def home(request):
    query = request.GET.get('q', '')
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)
    
    if query:
        products = products.filter(
            Q(name__icontains = query) |        # | means OR
            Q(description_icontains = query) |
            Q(category__name__icontains = query)
        )

    paginator = Paginator(products, 8)  # 8 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'inventory/home.html', {
        'categories': categories,
        # 'products': products  <-- This we remove after using the Paginator because our products then come from over there
        'page_obj': page_obj,
        'query': query,
    })

# Page for viewing products by category
def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category, is_active=True)


    return render(request, 'inventory/category.html', {
        'category': category,
        'products': products
    })