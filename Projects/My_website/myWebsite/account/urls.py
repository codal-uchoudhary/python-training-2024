from django.urls import path

from . import views 


urlpatterns = [
    path("",views.login,name="account_page"),
    path("signup",views.signup,name="signup_page")
]