from django.shortcuts import render, redirect
from .forms import NewProductForm
from .models import ProductImage
from django.contrib import messages
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
        