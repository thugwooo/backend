from django.urls import path, URLPattern, include
from .views import shoppingcart, shoppingcart_detail

urlpatterns = [
    path('shoppingcart', shoppingcart),
    path('shoppingcart-detail',shoppingcart_detail),
]
