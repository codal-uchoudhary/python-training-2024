from django.contrib.auth.models import User,auth
from . models import Post
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import blogSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination



class blog(APIView,LimitOffsetPagination):
    permission_classes = [AllowAny]

    def get(self,request):
        posts = Post.objects.all()
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(posts, request)
        serializers = blogSerializer(result_page, many=True, context={'request':request})
        return Response(serializers.data)

    
class userBlog(APIView,LimitOffsetPagination):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_item(self,id):
        try:
            item = Post.objects.get(id=id)
            return item
        except:
            return False
        
    def get(self,request):
        posts = Post.objects.filter(author=request.user.id)
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(posts, request)
        serializers = blogSerializer(result_page, many=True, context={'request':request})
        return Response(serializers.data)

    
    def post(self,request):
        data= request.data
        data['author']=request.user.id
        serializers = blogSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
    def put(self,request,id):
        obj = self.get_item(id=id)
        if not obj: return Response({'message':"please enter valid blog-slug"})
        if obj.author.id != request.user.id:
            return Response({'message':"You are not authorised to perform this action"})
        serializer = blogSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    
    def patch(self,request,id):   
        obj = self.get_item(id=id)
        if not obj: return Response({'message':"please enter valid blog-slug"})
        if obj.author.id != request.user.id:
            return Response({'message':"You are not authorised to perform this action"})
        if not obj: return Response({'message':"invalid blog-id"})
        serializer = blogSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
 
    def delete(self,request,id):
        obj = self.get_item(id=id)
        if obj==False: return Response({'message':"please enter valid blog id"})
        if obj.author.id != request.user.id:
            return Response({'message':"You are not authorised to perform this action"})
        obj.delete()
        return Response({'message':"blog deleted"})
    
    