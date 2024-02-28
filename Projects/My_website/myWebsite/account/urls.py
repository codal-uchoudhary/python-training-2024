from django.urls import path

from . import views 


urlpatterns = [
    path("",views.RegisterAPI.as_view()),
    path("login",views.LoginApi.as_view()),
    path("logout",views.Logout.as_view()),
    path("changePassword",views.UpdatePassword.as_view()),
    path("forgotPassword",views.ForgotPassword.as_view()),
    path("forgotPassword/<token>",views.ResetForgotedPassword.as_view())
]