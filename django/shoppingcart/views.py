from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Shoppingcart
from .serializers import ShoppingcartSerializer
# Create your views here.


@api_view(['POST','PATCH'])
def shoppingcart(request):

    if request.method == 'POST':      
        try :
            queryset = Shoppingcart.objects.get(
                u_id = int(request.POST['u_id']),
                p_id = int(request.POST['p_id'])
            )
        except :
            cart_info = Shoppingcart.inputShoppingcart(request)
            cart_info.save()
            return Response('create')
        else :
            queryset.s_count += 1
            queryset.save()
        return Response('count up')
    
    elif request.method == 'PATCH':
        queryset = Shoppingcart.objects.get(
            s_id = request.data.get('s_id')
        )
        queryset.s_count = int(request.data.get('s_count'))
        return Response('patch')

@api_view(['POST'])
def shoppingcart_detail(request):
    # 유저의 장바구니 
    if request.method == 'POST':
        queryset = Shoppingcart.objects.filter(
            u_id = int(request.POST['u_id'])
        )
        serializer = ShoppingcartSerializer(queryset, many = True)
        return Response(serializer)
    
