import os
import django
import csv
import sys
print(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'louishome.settings.local')
django.setup()
from product.models import Product

CSV_PATH_PRODUCTS = 'petfood.csv'

def str_to_list(data):
    data = data.replace(' ', '').replace('[', '').replace(']', '').replace("'",'').split(',')
    return data

with open(CSV_PATH_PRODUCTS,'r') as in_file:
    data_reader = csv.DictReader(in_file)

    for row in data_reader:
        
        # row['p_small_category1'] = str_to_list(row['p_small_category1'])
        # print(row['p_small_category1'], type(row['p_small_category1']))
        Product.objects.create(
            p_pet = row['p_pet'],
            p_name = row['p_name'],
            p_large_category = row['p_large_category'],      
            p_medium_category = row['p_medium_category'],
            p_small_category1 = str_to_list(row['p_small_category1']),  #브랜드
            p_small_category2 = str_to_list(row['p_small_category2']),
            p_small_category3 = str_to_list(row['p_small_category3']),
            p_small_category4 = str_to_list(row['p_small_category4']),
            p_small_category5 = str_to_list(row['p_small_category5']),
            p_small_category6 = str_to_list(row['p_small_category6']),
            p_small_category7 = str_to_list(row['p_small_category7']),
            p_small_category8 = str_to_list(row['p_small_category8']),
            p_ratail_price = int(row['p_retail_price']),
            p_wholesale_price = 0,
        )

