from blog.views import *
from django.urls import path,include

urlpatterns = [
    path('postApi',PostApi.as_view())
]
