from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register("all-blogs", views.blog)
router.register("my-blogs", views.myBlog)
router.register("blog-comments", views.blogComments)
router.register("add-blog-comment", views.addComment)

urlpatterns = [path("", include(router.urls))]
