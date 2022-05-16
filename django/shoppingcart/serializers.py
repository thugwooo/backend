from rest_framework import serializers
from .models import Shoppingcart

class ShoppingcartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoppingcart
        fields = '__all__'