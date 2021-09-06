from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters, mixins, viewsets
from rest_framework.response import Response
from base.helpers import CustomPagination
from booking.models import Booking
from .serializers import BookingSerializer, BookingListSerializer
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view, permission_classes
from datetime import datetime
from payment.models import Payment
from rest_framework.exceptions import ValidationError
from django.db.models import Sum

from booking.validation import booking_validation


class BookingViewset(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Booking.objects.filter()
    serializer_class = BookingSerializer
    pagination_class = CustomPagination
    lookup_field = 'pk'
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['-created_at']
    permission_classes = [permissions.IsAuthenticated, ]
    # permission_classes = [permissions.AllowAny, ]

    filterset_fields = [
        'customer_phone_no', 'room'
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return BookingListSerializer
        return BookingSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.email)

    def list(self, request, *args, **kwargs):
        return super(BookingViewset, self).list(request, *args, **kwargs)

    @method_decorator(booking_validation)
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['PATCH'])
# @permission_classes([permissions.IsAuthenticated])
@permission_classes([permissions.AllowAny])
def check_in(request, pk):
    try:
        booking = Booking.objects.get(pk=pk)
        booking.last_checkin_time = datetime.now().isoformat()

        paid_amount = Payment.objects.filter(booking=pk).aggregate(sum=Sum('amount'))
        paid_amount = paid_amount['sum'] if paid_amount['sum'] is not None else 0.0
        if paid_amount * 2 < Booking.objects.get(pk=pk).discounted_price:
            raise ValidationError(detail=f'Minimum 50% advance payment required before check in.')

        booking.updated_by = request.user.email
        return Response({
            'success': "true",
            'message': 'Customer successfully checked in.'
        }, status=status.HTTP_200_OK
        )
    except Booking.DoesNotExist:
        return Response({'message': 'Booking not found.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
@permission_classes([permissions.IsAuthenticated])
# @permission_classes([permissions.AllowAny])
def check_out(request, pk):
    try:
        booking = Booking.objects.get(pk=pk)
        booking.last_checkout_time = datetime.now().isoformat()

        paid_amount = Payment.objects.filter(booking=pk).aggregate(sum=Sum('amount'))
        paid_amount = paid_amount['sum'] if paid_amount['sum'] is not None else 0.0
        if paid_amount != Booking.objects.get(pk=pk).discounted_price:
            raise ValidationError(detail=f'Full payment required before check out.')

        booking.updated_by = request.user.email
        return Response({
            'success': "true",
            'message': 'Customer successfully checked out.'
        }, status=status.HTTP_200_OK
        )
    except Booking.DoesNotExist:
        return Response({'message': 'Booking not found.'}, status=status.HTTP_404_NOT_FOUND)
