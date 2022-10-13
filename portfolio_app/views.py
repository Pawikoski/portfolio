from django.shortcuts import render, HttpResponse
from .models import About


# Create your views here.
def index(request):
    about_info = About.objects.first()
    
    context = {
        "about": about_info
    }

    return render(request, "index.html", context=context)

