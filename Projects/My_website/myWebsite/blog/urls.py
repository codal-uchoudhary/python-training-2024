from django.urls import path

from . import views 

urlpatterns = [
    path("",views.startingPage,name="startingPage"),
    path("posts",views.posts,name="posts"),
    path("create",views.createBlog,name="createBlogPage"),
    path("posts/<slug>",views.postDetail,name="postDetail")
]
