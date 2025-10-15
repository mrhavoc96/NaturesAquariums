from django.contrib import admin
from .models import Category, Product
# Register your models here.


# Explanation available on Source
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('names',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'is_active', 'date_added')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'sku')
    readonly_fields = ('date_added', 'last_updated')