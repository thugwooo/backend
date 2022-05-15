from django.urls import path
from .views import login, register, pet, pet_register

urlpatterns = [
    path('login', login),
    path('register', register),
    path('pet-reg', pet_register),
    path('pet', pet)
]