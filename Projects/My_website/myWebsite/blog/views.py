from django.shortcuts import render,redirect
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
    
    return render(request,"blog/postDetail.html",{'post':iPost,"post_tag":iPost.tags.all()})

def createBlog(request):
    if request.method== 'POST':
        title = request.POST['title']
        excerpt = request.POST['excerpt']
        content = request.POST['content']
        tag = request.POST['tag']
        image = request.POST['file']

       
        if request.user.is_authenticated:

            first_name = request.user.first_name
            last_name = request.user.last_name
            email = request.user.email
            author=None

            author_exists=  Author.objects.get(email=email)
            if author_exists:
                author = author_exists
            else:
                first_name = request.user.first_name
                last_name = request.user.last_name
                email = request.user.email
                auth = Author(first_name = first_name,last_name=last_name,email = email)
                auth.save()
                author = auth
            
            blog = Post(title=title,excerpt=excerpt,content=content,slug=title,image_name=image, author=author)
            blog.save()
            messages.success(request, "Blog is posted Sucessfuly")
            return render(request,'blog/createBlog.html')


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
        return Response({'message':"this is post method "})
    def patch(self,request):
        return Response({'message':"this is patch method "})
    def delete(self,request):
        return Response({'message':"this is delete method "})

