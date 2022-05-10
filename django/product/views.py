from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .modules import str_to_list

# Create your views here.

@api_view(['GET','POST'])
def item_list(request):
    # 모든 데이터 가져오기
    if request.method =='GET':
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)
    # 한번에 입력
    elif request.method == 'POST':
        print(request.POST)
        return Response('asdf')
@api_view(['POST'])
def quration(request):
    print(request.POST)
    userData = request.POST
    userData._mutable = True
    petfood = Product.objects.filter(
        p_pet = userData['pet'],
        p_large_category ='사료',
    )
    serializers = ProductSerializer(petfood, many=True) 
    
    # print(serializers[0]['p_id'])
    # petfood = filtering.filteringAge(petfood,userData)
    # petfood = filtering.filteringAlg(petfood,userData)
    # print(len(petfood))

    #serializers 에 many=True 하지 않으면 에러난당
    
    return Response(serializers.data)
