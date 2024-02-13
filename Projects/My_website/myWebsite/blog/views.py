from django.shortcuts import render,redirect
from datetime import date
from . models import Post,Author
from django.contrib import messages


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

            if Author.objects.filter(email=email).exists():
                author = Author.objects.filter(email=email).first()
            else:
                first_name = request.user.first_name
                last_name = request.user.last_name
                email = request.user.email
                auth = Author(first_name = first_name,last_name=last_name,email = email)
                auth.save()
                author = Author.objects.filter(email=email).first()
            
            blog = Post(title=title,excerpt=excerpt,content=content,slug=title,image_name=image, author=author)
            blog.save()
            messages.success(request, "Blog is posted Sucessfuly")
            return render(request,'blog/createBlog.html')


        else:
            messages.success(request, "Please Login")
            return render(request,'blog/createBlog.html')





    else:
        return render(request,'blog/createBlog.html')
   