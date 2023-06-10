from .views import new_product, product_detail
from django.urls import path

app_name = "products"
urlpatterns = [
    path("new", new_product, name="new"),
    path("<int:product_id>/detail", new_product, name="detail"),
   
]