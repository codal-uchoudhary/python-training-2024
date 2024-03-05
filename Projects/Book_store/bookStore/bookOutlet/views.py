from django.shortcuts import render

from .models import Book

# Create your views here.
from django.db.models import Avg


def index(request):
    Books = Book.objects.all().order_by("price")
    totalBooks = Books.count()
    avg_rating = Books.aggregate(Avg("rating"))
    return render(
        request,
        "bookOutlet/index.html",
        {"Books": Books, "count": totalBooks, "avgrating": avg_rating},
    )


def bookDetail(request, id):
    book = Book.objects.get(pk=id)
    return render(
        request,
        "bookOutlet/bookDetail.html",
        {
            "title": book.title,
            "price": book.price,
            "author": book.author,
            "rating": book.rating,
        },
    )
    # return render(request,"bookOutlet/bookDetail.html")
