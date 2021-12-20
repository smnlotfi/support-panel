from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context={
        "name":"saman"
    }
    return render(request,'index.html',context)
