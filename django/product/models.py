from distutils.command.upload import upload
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_pet = models.CharField(max_length=20, default='강아지')
    p_name = models.CharField(max_length=100)
    p_brand = models.CharField(max_length=100)
    p_large_category = models.CharField(max_length=100, blank=True)
    p_medium_category = models.CharField(max_length=100, blank=True)
    p_small_category1 = ArrayField(models.CharField(max_length=20), blank =True)
    p_small_category2 = ArrayField(models.CharField(max_length=20), blank =True)
    p_small_category3 = ArrayField(models.CharField(max_length=20), blank =True)
    p_small_category4 = ArrayField(models.CharField(max_length=20), blank =True)
    p_small_category5 = ArrayField(models.CharField(max_length=20), blank =True)
    p_small_category6 = ArrayField(models.CharField(max_length=20), blank =True)
    p_small_category7 = ArrayField(models.CharField(max_length=20), blank =True)
    p_small_category8 = ArrayField(models.CharField(max_length=20), blank =True)
    p_ratail_price = models.IntegerField(blank=True)
    p_wholesale_price = models.IntegerField(blank=True, default=0)
    p_product_count = models.IntegerField(default=0)

    def __str__ (self):
        return self.p_name

class ProductPhoto(models.Model):
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/product/', blank =True)