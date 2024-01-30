from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')
def calculator(request):
    return render(request, 'calculator.html')

def result(request):
    num1 = int(request.GET['number_1'])
    num2 = int(request.GET['number_2'])
    oprator = request.GET['oprator']
    ans = None
    if oprator == '+':
        ans = num1+num2
    elif oprator == '-':
        ans = num1-num2
    elif oprator == '*':
        ans = num1*num2
    elif oprator == '/':
        ans = num1/num2
    else:
        ans = 'provide proper operator'
    return render(request, 'result.html',{'ans':ans})