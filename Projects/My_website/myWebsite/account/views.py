from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from rest_framework.views import APIView 
from .serializers import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.

class RegisterAPI(APIView):
    
    def post(self,request):
        data = request.data
        serializers = RegisterSerializers(data = data)
        if not serializers.is_valid():
            return Response({
                'status':False,
                'messages':serializers.errors
            })
        else:
            serializers.save()
            return Response({'status':True,'message':"user is created"})

class LoginApi(APIView):
    def post(self,request):
        data = request.data
        serializers = LoginSerializers(data=data)
        if not serializers.is_valid():
            return Response({
                'status':False,
                'message':serializers.errors
            })
        else:
            user = authenticate(username = serializers.data['username'],password = serializers.data['password'])
            if not user:
                return Response({'message':"user is not found"})
            token = Token.objects.get_or_create(user=user)
            return Response({'status':True,'message':"user is loged", 'token':str(token),'first_name':user.first_name,'email':user.email})
