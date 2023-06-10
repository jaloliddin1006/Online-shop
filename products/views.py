from django.shortcuts import render, redirect
from .forms import NewProductForm
from .models import ProductImage, Product
from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.


def new_product(request):
    if request.method == "GET":
        form = NewProductForm()
        return render(request, "product_new.html", {"form":form})
    if request.method == "POST":
        form = NewProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            product = form.save(request)
            for image in request.FILES.getlist("images"):
                ProductImage.objects.create(image=image, product=product)
            messages.success(request,"Yangi maxsulot yaratildi")
            return redirect("main:index")
        return render(request, "product_new.html", {"form":form})
        
        
        
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "product_detail.html", {"product":product})