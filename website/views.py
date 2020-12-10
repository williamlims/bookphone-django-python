from django.shortcuts import render

def home(request):
    return render(request, "website/home.html")
    
def base(request):
    return render(request, "website/base.html")

def register(request):
    return render(request, "website/register.html")