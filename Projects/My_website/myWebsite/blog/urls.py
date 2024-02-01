from django.urls import path

from . import views 

urlpatterns = [
    path("",views.startingPage,name="startingPage"),
    path("posts",views.posts,name="posts"),
    path("posts/<slug>",views.postDetail,name="postsDetail")
]
