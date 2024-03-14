from django.contrib.auth.models import User, auth
from .models import Post, Comments, Like
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import (
    blogSerializer,
    CommentSerializer,
    BlogCommentsSerialiser,
    UserSerializer,
    LikeBlogSerializer,
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


class LikeBlog(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LikeBlogSerializer


class GetLikeBlog(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, blog):
        blog = Post.objects.get(id=blog)
        obj = Like.objects.get(blog=blog)
        data = obj.people.all()
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data)
