from django.shortcuts import render,get_object_or_404
from datetime import date
from . models import Post



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
    return render(request,'blog/createBlog.html')