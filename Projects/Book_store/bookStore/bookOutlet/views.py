from django.shortcuts import render

from .models import Book
# Create your views here.

def index(request):
    Books = Book.objects.all()
    return render(request,'bookOutlet/index.html',{'Books':Books})

def bookDetail(request,id):
    Books = Book.objects.get(pk=id)
    return(request,'bookOutlet/bookDetail.html')