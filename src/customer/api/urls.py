from django.urls import path
from .views import CustomerViewset

app_name = 'customer'

customer_list = CustomerViewset.as_view({
    'get': 'list',
    'post': 'create'
})
customer_detail = CustomerViewset.as_view({
    'get': 'retrieve',
    'patch': 'update'
})

urlpatterns = [
    path('', customer_list, name='customer-list'),
    path('<int:pk>/', customer_detail, name='customer-detail'),
]
