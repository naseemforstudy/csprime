from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

def index(request):
    return HttpResponse("This is your first view")
@api_view(["GET"])
def checkPrime(request):
    num = int(request.GET.get("num"))
    counter = 0
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                counter = 0
                break
            else:
                counter=1
    else:
        status="The given number must be grater than one"
    if (counter) == 1:
        status = "This number is a prime number"
    elif (num) == 2:
         status = "This number is a prime number"
    else:
        status = "This number is not a prime number"
    return Response(status)
        
    
    
    


    

    
