from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from . models import Post
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import blogSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404





class crudBlogApi(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = blogSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        userid = request.user.id
        datalist = list(self.queryset)
        serializers = blogSerializer(datalist,many=True)
        return Response(serializers.data)
    
    