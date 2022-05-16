from django.contrib import admin
from .models import User
from shoppingcart.models import Shoppingcart
# Register your models here.


class ShoppingcartInline(admin.TabularInline):
    model = Shoppingcart

class UserAdmin(admin.ModelAdmin):
    inlines = [ShoppingcartInline,]
    list_display = ('u_id', 'u_name', )

admin.site.register(User, UserAdmin)