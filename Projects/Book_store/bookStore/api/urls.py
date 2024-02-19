from bookForm import views 
from django.urls import path

urlpatterns = [
    path('',views.form.as_view()),
]
