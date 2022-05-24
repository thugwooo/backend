from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from .models import UserAddress, UserOrderDetail
from user.models import User
# Create your views here.

@api_view(['POST'])
def order(request):
    if request.method == 'POST':
        try :
            # UserAddress.objects.get(u_id = int(request.POST['u_id']))
            userorderDetail_info = UserOrderDetail()
            userorderDetail_info.u_id = User(u_id = int(request.POST['u_id']))
            userorderDetail_info.p_id = Product(p_id = int(request.POST['p_id']))
            userorderDetail_info.save()
            print('detail')
        except :
            userorder_info = UserAddress()
            userorder_info.u_id = User(u_id = int(request.POST['u_id']))
            userorder_info.save()
            

        else:
            print('else')
        return Response('성공')