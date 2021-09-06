from django.urls import path
from .views import RoomViewset

app_name = 'room'

room_list = RoomViewset.as_view({
    'get': 'list',
    'post': 'create'
})
room_detail = RoomViewset.as_view({
    'get': 'retrieve',
    'patch': 'update'
})

urlpatterns = [
    path('', room_list, name='room-list'),
    path('<int:pk>/', room_detail, name='room-detail'),
]
