from django.shortcuts import render
from django.views import View
from products.models import Product, Category
from django.shortcuts import get_object_or_404
# Create your views here.

def all_page_view_category(request):
    categorys = Category.objects.all()
    return {"categorys":categorys}


class IndexView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'index.html', {'products':products})
    
class CategoryView(View):
    def get(self, request, category_name):
        category = get_object_or_404(Category, name=category_name)
        products = Product.objects.filter(category=category)
        return render(request, "category.html", {'products':products, "category":category})