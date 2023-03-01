from django.urls import path
from . import views
app_name = 'finder'


urlpatterns = [
    path( '' ,views.rommseterslist , name='serachers_list' ),


]