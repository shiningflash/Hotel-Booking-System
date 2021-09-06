import json
from rest_framework.exceptions import ValidationError
from rest_framework import status
from django.db.models import Sum
from rest_framework.response import Response

from booking.models import Booking
from payment.models import Payment
from room.models import Room


def booking_validation(func):
    def validation(request, *args, **kwargs):
        try:
            body = request.body.decode()
            if not body:
                raise ValidationError(
                    detail='Required information missing', code=status.HTTP_400_BAD_REQUEST
                )
            body = json.loads(body)
            room = body.get('room', None)
            required_capacity = body.get('required_capacity', None)
            booking_start_time = body.get('booking_start_time', None)
            booking_end_time = body.get('booking_end_time', None)

            if not room or not booking_start_time or not booking_end_time:
                raise ValidationError(
                    detail='Required information missing', code=status.HTTP_400_BAD_REQUEST
                )

            booking_list = Booking.objects.filter(room=room)

            if booking_list.filter(booking_start_time__gte=booking_start_time,
                                   booking_start_time__lte=booking_end_time).exists() \
                or booking_list.filter(booking_end_time__gte=booking_start_time,
                                       booking_end_time__lte=booking_end_time).exists():
                raise ValidationError(detail=f'Room is not available between the given time range.')

            if required_capacity > Room.objects.get(pk=room).capacity:
                raise ValidationError(detail=f'Room capacity is not sufficient.')
        except Room.DoesNotExist:
            return Response({'message': 'Room not found.'}, status=status.HTTP_404_NOT_FOUND)
        return func(request, *args, **kwargs)
    return validation


def payment_check(func):
    def validation(request, *args, **kwargs):
        pk = kwargs.get('pk')
        paid_amount = Payment.objects.filter(booking=pk).aggregate(sum=Sum('amount'))
        paid_amount = paid_amount['sum'] if paid_amount['sum'] is not None else 0.0
        if paid_amount * 2 < Booking.objects.get(pk=pk).discounted_price:
            raise ValidationError(detail=f'Minimum 50% advance payment required before check in.')
        return func(request, *args, **kwargs)
    return validation


def full_payment_check(func):
    def validation(request, *args, **kwargs):
        pk = kwargs.get('pk')
        paid_amount = Payment.objects.filter(booking=pk).aggregate(sum=Sum('amount'))
        paid_amount = paid_amount['sum'] if paid_amount['sum'] is not None else 0.0
        if paid_amount != Booking.objects.get(pk=pk).discounted_price:
            raise ValidationError(detail=f'Full payment required before check out.')
        return func(request, *args, **kwargs)
    return validation
