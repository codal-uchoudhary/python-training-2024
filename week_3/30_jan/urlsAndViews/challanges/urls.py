from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("<int:month>", views.monthly_challenge_by_int),
    path("<str:month>", views.monthly_challenge, name="myUrl"),
]

# reverse function
