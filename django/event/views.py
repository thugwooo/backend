from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Event

# Create your views here.


@api_view(['POST'])
def event(request):
    #이벤트 아이템 리스트 return
    if request.method == 'POST':
        queryset = Event.objects.get(e_name = request.POST['e_name'])
        
        return Response()