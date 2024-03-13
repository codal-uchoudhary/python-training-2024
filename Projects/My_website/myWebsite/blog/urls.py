from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register("all-blogs", views.Blog)
router.register("my-blogs", views.MyBlog)
router.register("blog-comments", views.BlogComments)
router.register("new-blog-comment", views.AddComment)

urlpatterns = [path("", include(router.urls))]
