from django.db import models

# Create your models here.

cats = [
        ('Electronics' , 'Electronics'),
        ('Clothing', 'Clothing'),
        ('Other', 'Other'),
        ]

class Product(models.Model):
    name = models.CharField(max_length=100, default='name' ,verbose_name='Product Name')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='product/imgs/%Y/%m/%d/', default='product/imgs/default.jpg')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50, blank=True, null=True, choices=cats)


    def __str__(self):
        return self.name
    
    class Meta:
            verbose_name = 'Product'
            ordering = ['-price']