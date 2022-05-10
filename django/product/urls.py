from django.urls import path
from .views import item_list,quration

urlpatterns = [
    path('items', item_list),
    path('quration', quration),
]