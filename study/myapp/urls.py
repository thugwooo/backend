from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.index),
    path('create/', views.create ),
    path('read/<int:id>/', views.read),
]