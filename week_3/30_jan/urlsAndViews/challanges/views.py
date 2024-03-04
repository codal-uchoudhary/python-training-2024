from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


challenge_dict = {
    "january": "30 pushUp ebery day",
    "febuary": "2km running every day",
    "march": "reading bool every day",
    "aprail": "5 liter of water every day",
    "may": "5 liter of water every day",
    "june": "5 liter of water every day",
    "july": "5 liter of water every day",
    "auguest": "5 liter of water every day",
    "octomber": "5 liter of water every day",
    "november": "5 liter of water every day",
    "december": "5 liter of water every day",
}


def index(request):
    list_item = list(challenge_dict.keys())
    list_data = ""
    for i in list_item:
        list_data += f'<li><a href="{i}"><h1>{i}</h1></a></l1>'

    data = f"<ul>{list_data}</ul>"
    return HttpResponse(data)


def monthly_challenge(request, month):
    try:
        text = challenge_dict[month]
        return HttpResponse(f"<h1>{text}</h1>")
    except:
        return HttpResponse("page not found")


def monthly_challenge_by_int(request, month):
    months = list(challenge_dict.keys())
    forward_month = months[month - 1]
    link = reverse("myUrl", args=[forward_month])
    return HttpResponseRedirect(link)
