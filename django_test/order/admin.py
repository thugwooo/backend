from django.contrib import admin
from .models import UserAddress, UserOrderDetail
# Register your models here.

admin.site.register(UserAddress)
admin.site.register(UserOrderDetail)