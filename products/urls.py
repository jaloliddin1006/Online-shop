from .views import new_product
from django.urls import path

app_name = "product"
urlpatterns = [
    path("new/", new_product, name="new"),
   
]