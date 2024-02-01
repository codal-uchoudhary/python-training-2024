from django.shortcuts import render

def startingPage(request):
    return render(request,'blog/index.html')

def posts(request):
    pass

def postDetail(request):
    pass


