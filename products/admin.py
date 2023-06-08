from django.contrib import admin
from .models import Product, Category, Comments, ProductImage
# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'author', 'date']
    inlines = [ProductImageInline]
    
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Comments)