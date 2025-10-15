from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100, unique = True)

    class Meta:         #special inner class in Django used for holding metadata
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):      #It's a dunder function, Its only job is to define how an object should look when you convert it to a string
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'products')

    name = models.CharField(max_length = 200)
    sku = models.CharField(max_length=50, blank=True, null=True, unique=True) #SKU stands for Stock keeping Unit is essentially a unique product id
    description = models.TextField(blank=True) #Unlike CharField, TextField has no max length
    price = models.DecimalField(max_digits = 9, decimal_places = 2)
    stock = models.PositiveIntegerField(default = 0)

    image = models.ImageField(upload_to='products/', default = 'products/default.jpg',blank = True, null = True)
    is_active = models.BooleanField(default = True)   #Boolean toggle- lets the owner hide a product from customers without deleting it.
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
        indexes = [
            models.Index(fields = ['name']),
            models.Index(fields = ['sku']),
        ]

    def __str__(self):
        return f"{self.name} ({self.category.name})"  #produces essentially the human readable name of the Object being printed 

