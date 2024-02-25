from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views 


urlpatterns = [
    path("",views.blog.as_view()),
    path("myBlogs",views.userBlog.as_view()),
    path("myBlogs/<slug>",views.userBlog.as_view())
]
