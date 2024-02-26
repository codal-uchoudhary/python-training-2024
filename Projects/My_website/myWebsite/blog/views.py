from django.contrib.auth.models import User,auth
from . models import Post
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import blogSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView





class blog(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        posts = Post.objects.all()
        serializers = blogSerializer(posts,many=True)
        return Response(serializers.data)

    
class userBlog(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        posts = Post.objects.filter(author=request.user.id)
        serializers = blogSerializer(posts,many=True)
        return Response(serializers.data)
    
    def put(self,request):
        return Response({'message':"this is put method (under devlopment)"})
    def delete(self,request):
        return Response({'message':"this is get method (under devlopment)"})   
    def patch(self,request):
        return ({'message':"this is patch method (under devlopment)"})
    
    