from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"", views.myBlog)

router2 = routers.DefaultRouter()
router2.register(r"", views.blog)
urlpatterns = [
    path("", include(router2.urls)),
    path("myblog", include(router.urls)),
]
