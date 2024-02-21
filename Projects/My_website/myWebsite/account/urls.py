from django.urls import path

from . import views 


urlpatterns = [
    path("",views.RegisterAPI.as_view()),
    path("login",views.LoginApi.as_view())
    # path("",views.account,name="account_page"),
    # path("logout",views.logout,name="logout"),
    # path("login",views.login,name="login_page"),
    # path("signup",views.signup,name="signup_page")
]