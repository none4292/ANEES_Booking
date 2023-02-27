from django.urls import path, re_path
from .views import rommseterslist, RoomDetail , NewProperty

app_name = 'roommseters'

urlpatterns = [
    path('list',rommseterslist,name='room_list'),
    path('list/<int:id>',RoomDetail,name='room_detail'),
    path('list/create',NewProperty.as_view(),name='add_property'),
]