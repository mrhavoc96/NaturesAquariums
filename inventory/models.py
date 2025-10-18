from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        # Defines how category objects appear in admin panels or print statements
        return self.name



class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    name = models.CharField(max_length=200)
    sku = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=True,
        help_text="Stock Keeping Unit – unique product ID"
    )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    # Explicitly mentioning the storage path for images to cloudinary
    image = models.ImageField(
        storage=MediaCloudinaryStorage(),
        upload_to='products/',
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True,
        help_text="Toggle to hide product without deleting it."
    )
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['sku']),
        ]

    def __str__(self):
        # Returns human-readable name for the product object
        return f"{self.name} ({self.category.name})"
