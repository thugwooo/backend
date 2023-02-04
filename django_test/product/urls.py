from django.urls import path
from .views import item_list,item_detail,quration

urlpatterns = [
    path('items', item_list),
    path('item/<int:p_id>',item_detail),
    path('quration', quration),
]