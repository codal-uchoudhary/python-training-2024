from django.urls import path

from . import views 


urlpatterns = [
    path("",views.RegisterAPI.as_view()),
    path("login",views.LoginApi.as_view()),
    path("logout",views.Logout.as_view()),
    path("changePassword",views.ResetPassword.as_view())
]