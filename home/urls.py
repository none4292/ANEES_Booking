from django.urls import path, re_path
from .views import homeview
app_name = 'home'

urlpatterns = [
    path('' , homeview , name='home'),
]