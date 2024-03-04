from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.views import APIView 
from .serializers import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
import uuid
from .models import Profile
from .Email.ForgotPasswordEmail import *

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

class Logout(APIView):
    def get(self,request):
        request.user.auth_token.delete()
        return Response({'message':"successfully logut"})
    
class UpdatePassword(APIView):
    def post(self,request):
        serializers = ChangePasswordSerializer(data = request.data)
        if serializers.is_valid():
            user = request.user
            if user.check_password(serializers.data.get('old_password')):
                user.set_password(serializers.data.get('new_password'))
                user.save()
                return Response({'message':"password is changed"})
            else:
                return Response({'message':"old password is not correct"})
        else:
            return Response(serializers.errors)
        
class ForgotPassword(APIView):
    def post(self,request):
        serializers = UsernameSerializer(data=request.data)
        if serializers.is_valid():
            obj = User.objects.get(username = serializers.data.get('username'))
            if not obj:
                return Response({'message':"wrong username"})
            token = str(uuid.uuid4())
            try:
                profile_obj = Profile(forget_password_token=token,user=obj)
                profile_obj.save()
            except:
                profile_obj = Profile.objects.get(user=obj)
                profile_obj.forget_password_token = token
                profile_obj.save()
            send_forgot_password_mail(obj.email,token)
            return Response({"message":"email is send"})
        else:
            return Response(serializers.errors)


class ResetForgotedPassword(APIView):
    def post(self,request,token):
        obj = Profile.objects.get(forget_password_token=token)
        user = obj.user
        serializer = ResetPasswordSerializer(data = request.data)
        if serializer.is_valid():
            user.set_password(serializer.data.get('password'))
            user.save()
            return Response({'message':"password change successfully"})
        else:
            return Response({'message':"enter valid data"})