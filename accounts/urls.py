from django.urls import path, re_path

from .views import signup , profile , profile_edit, delete_post

app_name = 'accounts'

urlpatterns = [
    path('signup',signup , name='signup'),
    path('profile/',profile,name='profile'),
    path('profile/edit', profile_edit , name='profile_edit') ,
    path('profile/delete_post/<str:id>/',delete_post, name='delete_post') ,

]