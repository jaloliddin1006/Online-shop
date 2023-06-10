from django.shortcuts import render
from .forms import NewProductForm
# Create your views here.


def new_product(request):
    form = NewProductForm
    return render(request, "product_new.html", {"form":form})