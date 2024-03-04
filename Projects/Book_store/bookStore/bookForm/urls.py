from django.urls import path
from . import views

urlpatterns = [
    # path("",views.form),
    path("/users", views.users),
    path("/registration", views.registration, name="regiser_page"),
    path("/login", views.login, name="login_page"),
    path("/logout", views.logout),
]
