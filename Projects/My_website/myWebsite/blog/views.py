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

    def get_item(self,slug):
        item = Post.objects.get(slug=slug)
        if item:
            return item
        else:
            return False
        
    def get(self,request):
        posts = Post.objects.filter(author=request.user.id)
        serializers = blogSerializer(posts,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        data = request.data
        data['author']=request.user.id
        serializers = blogSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
    def put(self,request,slug):
        data = request.data
        if data['author'] != request.user.id:
            return Response({'message':"you are not valid author"})
        obj = self.get_item(slug)
        if obj==False : return Response({'message':"in valid slug"})
        serializer = blogSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def patch(self,request,slug):   
        data = request.data
        if data['author'] != request.user.id:
            return Response({'message':"you are not valid author"})
        obj = self.get_item(slug)
        if obj==False : return Response({'message':"in valid slug"})
        serializer = blogSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
 
    def delete(self,request,slug):
        data = request.data
        if data['author']!=request.user.id :
            return Response({'message':'you are not valid author'})
        obj = self.get_item(slug)
        if obj==False : return Response({'message':"in valid slug"})
        obj.delete()
        return Response({'message':"blog deleted"})
    
    