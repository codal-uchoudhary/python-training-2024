from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views 


urlpatterns = [
    path("",views.blog.as_view()),
    path("blogs/",views.userBlog.as_view()),
    path("blogs/<id>",views.userBlog.as_view())
]
