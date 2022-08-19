from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PetSerializer, UserSerializer
from .models import User,Pet
# Create your views here.


@api_view(['POST'])
def register(request):
    #회원가입
    if request.method =='POST':
        u_info = User.registerUser(request)
        try: 
            user_info = User.objects.get(u_strid = request.POST['u_strid'])
            # User(u_strid = request.POST['u_strid']).save()
        # except User.DoseNotexist
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

# 펫 model save
@api_view(['POST','UPDATE','PUT',"PATCH"])
def pet_register(request):
    if request.method == 'POST':
        p_info = Pet.inputPet(request)
        try:
            pet_info = Pet.objects.get(
                u_id = User.objects.get(u_id = request.POST['u_id']),
            )
        except:
            # p_info.save()
            print('asdf')
            return Response('register')
        #여기를 어떻게 해야 잘했다고 소문이 날까
    elif request.method =='PATCH':
        print(request.data['asdf'])
        return Response('ㅁㄴㅇㄹ')
    return Response('실패')

@api_view(['POST'])
def pet(request):
    if request.method =='POST':
        try : 
            pet_info = Pet.objects.filter(
                u_id = User.objects.get(u_id = request.POST['u_id'])
            )
        except :
            return Response('no pet')
        else: 
            serializer = PetSerializer(pet_info, many = True)
            return Response(serializer)


