from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Users 

# Create your views here.

def form(request):
    if request.method == 'POST':
        name = request.POST['uname']
        newUser = Users(username=name)
        newUser.save()
        return HttpResponseRedirect("form/users")

    return render(request,"bookForm/form.html")


def users(request):

    list = Users.objects.all()

    return render(request,"bookForm/users.html",{"users":list})