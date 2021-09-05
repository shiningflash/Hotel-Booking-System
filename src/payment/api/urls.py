from django.urls import path
from .views import PaymentViewset

app_name = 'payment'

payment_list = PaymentViewset.as_view({
    'get': 'list',
    'post': 'create'
})
payment_detail = PaymentViewset.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', payment_list, name='payment-list'),
    path('<int:pk>/', payment_detail, name='payment-detail'),
]
