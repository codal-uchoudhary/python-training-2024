from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"myblog", views.myBlog)

router2 = routers.SimpleRouter()
router2.register(r"blog", views.blog)

router_blog_app = routers.DefaultRouter()
router_blog_app.extend(router)
router_blog_app.extend(router2)


urlpatterns = [
    path("", include(router_blog_app.urls)),
]
