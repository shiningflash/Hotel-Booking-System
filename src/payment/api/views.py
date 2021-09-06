from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters, mixins, viewsets
from rest_framework.response import Response
from base.helpers import CustomPagination
from payment.models import Payment
from .serializers import PaymentSerializer
from django.utils.decorators import method_decorator

from payment.validation import payment_validation


class PaymentViewset(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Payment.objects.filter()
    serializer_class = PaymentSerializer
    pagination_class = CustomPagination
    lookup_field = 'pk'
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['-created_at']
    permission_classes = [permissions.IsAuthenticated, ]
    # permission_classes = [permissions.AllowAny, ]

    filterset_fields = [
        'booking', 'amount', 'payment_method'
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.email)

    def list(self, request, *args, **kwargs):
        return super(PaymentViewset, self).list(request, *args, **kwargs)

    @method_decorator(payment_validation)
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
