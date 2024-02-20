from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from . models import Post
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import blogSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny



class crudBlogApi(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = blogSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes=[IsAuthenticated]
    

   