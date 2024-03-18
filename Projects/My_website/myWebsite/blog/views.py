from django.contrib.auth.models import User
from .models import Post, Comments
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import (
    blogSerializer,
    CommentSerializer,
    BlogCommentsSerialiser,
    UserSerializer,
)
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from django.core.cache import cache


""" class to get all the blogs """


class Blog(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = blogSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        data = cache.get("posts", None)
        if data:
            return data
        data = Post.objects.all()
        cache.set("posts", data)
        return data


""" class to get comments of a specific blog """


class BlogComments(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogCommentsSerialiser
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


""" class to add comments on a specific blog """


class AddComment(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


""" class to get user-specific blogs """


class MyBlog(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = blogSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_item(self, id):
        try:
            item = Post.objects.get(id=id)
            return item
        except:
            return False

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user.id)

    def destroy(self, request, pk):
        obj = self.get_item(id=pk)
        if obj == False:
            return Response({"message": "please enter valid blog id"})
        if obj.author.id != request.user.id:
            return Response(
                {"message": "You are not authorised to perform this action"}
            )
        obj.delete()
        return Response({"message": "blog deleted"})

    def partial_update(self, request, pk):
        obj = self.get_item(id=pk)
        if not obj:
            return Response({"message": "please enter valid blog-slug"})
        if obj.author.id != request.user.id:
            return Response(
                {"message": "You are not authorised to perform this action"}
            )
        if not obj:
            return Response({"message": "invalid blog-id"})
        serializer = blogSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


""" class to like a blog"""


class LikeTheBlogTest(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            blog = Post.objects.get(id=request.data["blog-id"])
            obj = blog.like.filter(id=request.user.id)
            if obj.exists():
                blog.like.remove(request.user.id)
                return Response({"you disliked the blog"})
            blog.like.add(request.user.id)
            blog.save()
            return Response({"you liked this blog"})
        except Exception as e:
            raise e


class GetLikeBlog(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            blog = Post.objects.get(id=request.data["blog-id"])
            people = blog.like.all()
            serializer = UserSerializer(people, many=True)
            return Response(serializer.data)
        except Exception as e:
            raise e
