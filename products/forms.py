from django import forms
from .models import Product

class NewProductForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={"allow_multiple_selected":True}))
    class Meta:
        model = Product
        fields = ("category", "title", "description", "price", "address", "phone_number", "tg_username")