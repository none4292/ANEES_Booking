from django.shortcuts import render
from roommseters.models import Place
# Create your views here.


# retreve the places from database and open the home page
def homeview(request): 
   obj = Place.objects.all()
   return render(request,'home/homepage.html',{'obj':obj})