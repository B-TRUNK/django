from django.contrib import admin
from .models import Product, test

# Below class is to adjust admin panel for product table
class ProductAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'price', 'active']
    list_display_links = ['price']
    #note editables should not be in links
    list_editable   = ['name', 'active']
    #search bar
    search_fields = ['name', 'price']
    #filtering
    list_filter = ['category', 'price']



# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(test)



