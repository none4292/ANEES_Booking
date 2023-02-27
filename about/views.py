from django.shortcuts import render
from .models import About
# Create your views here.
def about_us(request):
    about = About.objects.last()
    return render(request, 'about/about_us.html',{'about':about})