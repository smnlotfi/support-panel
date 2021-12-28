from django.http import HttpResponse
from django.shortcuts import render



def header(request):
    context={
       
    }
    return render(request,'layouts/header.html',context)

def footer(request):
    context={
    }
    return render(request,'layouts/footer.html',context)

def home_page(request):
    context={
    }
    return render(request,'index.html',context)
