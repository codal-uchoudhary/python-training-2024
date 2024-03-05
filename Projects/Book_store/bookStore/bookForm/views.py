from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

from .models import Users

# Create your views here.

# def form(request):
#     if request.method == 'POST':
#         name = request.POST['uname']
#         age = request.POST['age']
#         newUser = Users(username=name,age=age)
#         newUser.save()
#         return HttpResponseRedirect("form/users")

#     return render(request,"bookForm/form.html")


class form(APIView):
    def get(self, request):
        obj = Users.objects.all()
        serializer = userSeriallizers(obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializers = userSeriallizers(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)

    def put(self, request):
        data = request.data
        serializers = userSeriallizers(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)

    def patch(self, request):
        data = request.data
        obj = Users.objects.get(id=data["id"])
        serializers = userSeriallizers(obj, data=data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)

    def delete(self, request):
        data = request.data
        obj = Users.objects.get(id=data["id"])
        obj.delete()
        return Response({"message": "item is deleted"})


def registration(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.info(request, "username is exist")
        elif User.objects.filter(email=email).exists():
            messages.info(request, "email is already used")
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )
            user.save()
            print("user created")
            return HttpResponseRedirect("/")

    return render(request, "bookForm/register.html")


def users(request):
    list = Users.objects.all()

    return render(request, "bookForm/users.html", {"users": list})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            messages.info(request, "invalid credential")
            return render(request, "bookForm/login.html")
    else:
        return render(request, "bookForm/login.html")


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/form")
