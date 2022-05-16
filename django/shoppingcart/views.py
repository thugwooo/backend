from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Shoppingcart
# Create your views here.


@api_view(['GET','POST'])
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

