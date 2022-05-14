from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User,Pet
# Create your views here.


@api_view(['POST'])
def register(request):
    #회원가입
    if request.method =='POST':
        u_info = User.registerUser(request)
        try: 
            user_info = User.objects.get(u_strid = request.POST['u_strid'])
        except:
            print('done')
            u_info.save()
            return Response('register')
        else : 
            return Response('fail')

@api_view(['POST'])
def login(request):
    if request.method =='POST':
        try:
            user_info = User.objects.get(
                u_strid = request.POST['u_strid'],
                u_pw = request.POST['u_pw']
            )
            serializer = UserSerializer(user_info)
        except:
            return Response('fail')
        else :
            print('done')
            return Response(serializer.data)
@api_view(['POST'])
def pet_register(request):
    if request.method == 'POST':
        try:
            pet_info = Pet.objects.get(
                u_id = User.objects.get(u_id = request.POST['u_id']),
            )
        except:
        #여기를 어떻게 해야 잘했다고 소문이 날까
