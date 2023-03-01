from django.shortcuts import render
from .models import About
# Create your views here.
# retreve all the last about model from database
def about_us(request):
    about = About.objects.last()
    return render(request, 'about/about_us.html',{'about':about})