from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='mainurl'),
    path('<int:month>',views.monthlyChallengeByInt),
    path('<str:month>',views.monthlyChallenge,name='myUrl')

]