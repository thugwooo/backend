from rest_framework import serializers
from .models import Product, ProductPhoto

class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ProductPhoto
        fields = ['image', 'p_id']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductPhotoSerializer(many=True, read_only =True)
    class Meta:
        model = Product
        fields = '__all__'