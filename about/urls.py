from django.urls import path, re_path
from .views import about_us

app_name = 'about'

urlpatterns = [
    path('about_us',about_us,name='about')
]