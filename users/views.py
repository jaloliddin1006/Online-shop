from django.shortcuts import render, redirect
from users.forms import SignupForm
from django.views import View
from django.contrib import messages
# Create your views here.


class SignupView(View):
    def get(self, request):
        return render(request, "registration/signup.html", {"form":SignupForm()})
    
    def post(self, request):
        form = SignupForm(data=request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Muvaffaqiyatli yaratildi")
            return redirect('login')
        return render(request, "registration/signup.html", {"form":form})
            