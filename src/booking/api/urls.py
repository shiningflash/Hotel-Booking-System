from django.urls import path
from .views import BookingViewset, check_in, check_out

app_name = 'booking'

booking_list = BookingViewset.as_view({
    'get': 'list',
    'post': 'create'
})
booking_detail = BookingViewset.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', booking_list, name='booking-list'),
    path('<int:pk>/', booking_detail, name='booking-detail'),
    path('<int:pk>/checkin/', check_in, name='check-in'),
    path('<int:pk>/checkout/', check_out, name='check-out'),
]
