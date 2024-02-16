from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from datetime import date
from . models import Post,Author
from django.contrib import messages
from rest_framework.response import Response
from .serializers import blogSerializer
from rest_framework.views import APIView


def startingPage(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request,'blog/index.html',{"posts":latest_posts})

def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request,'blog/allPost.html',{"posts":all_posts})

def postDetail(request,slug):
    iPost = Post.objects.all().get(slug = slug)
    author_id = iPost.author_id
    author = Author.objects.get(id =author_id).user
    return render(request,"blog/postDetail.html",{'post':iPost,"post_tag":iPost.tags.all(),'author':author})

def createBlog(request):
    if request.method== 'POST':
        title = request.POST['title']
        excerpt = request.POST['excerpt']
        content = request.POST['content']
        tag = request.POST['tag']
        image = request.POST['file']

        id  = request.user.id
        if request.user.is_authenticated:
            author, created =  Author.objects.get_or_create(user=request.user)
            blog = Post(title=title,excerpt=excerpt,content=content,slug=title,image_name=image, author=author)
            blog.save()
            messages.success(request, "Blog is posted Sucessfuly")
            return redirect('/posts')
        else:
            messages.success(request, "Please Login")
            return render(request,'blog/createBlog.html')
    else:
        return render(request,'blog/createBlog.html')

class PostApi(APIView):
    def get(self,request):
        data = Post.objects.all()
        serializerData = blogSerializer(data,many=True)
        return Response(serializerData.data)
    
    def post(self,request):
        data = request.data
        serializer = blogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def patch(self,request):
        data = request.data
        serializer = blogSerializer(data = data,partial=True)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self,request):
        data = request.data
        obj = Post.objects.get(id=data['id'])
        obj.delete()
        return Response({'message':"data is deleted"})

