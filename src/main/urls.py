from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Hotel Booking System API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('account.api.urls', 'account_api')),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/cutomer/', include('customer.api.urls', 'customer_api')),
    path('api/room/', include('room.api.urls', 'room_api')),
    path('api/booking/', include('booking.api.urls', 'booking_api')),
    path('api/payment/', include('payment.api.urls', 'payment_api')),

    path('swagger/', schema_view)
]
