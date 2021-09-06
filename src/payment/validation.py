import json
from rest_framework.exceptions import ValidationError
from rest_framework import status
from django.db.models import Sum

from booking.models import Booking
from payment.models import Payment


def payment_validation(func):
    def validation(request, *args, **kwargs):
        body = request.body.decode()
        if not body:
            raise ValidationError(
                detail='Required information missing', code=status.HTTP_400_BAD_REQUEST
            )
        body = json.loads(body)
        booking = body.get('booking', None)
        amount = body.get('amount', None)

        if not booking or not amount:
            raise ValidationError(
                detail='Required information missing', code=status.HTTP_400_BAD_REQUEST
            )
        if amount <= 0:
            raise ValidationError(
                detail='Please, enter a positive number. Negative not allowed.', code=status.HTTP_400_BAD_REQUEST
            )

        paid_amount = Payment.objects.filter(booking=booking).aggregate(sum=Sum('amount'))
        due = Booking.objects.get(pk=booking).discounted_price - paid_amount['sum'] if paid_amount['sum'] is not None else 0.0

        if amount > due:
            raise ValidationError(
                detail='Payment can not be more than due.', code=status.HTTP_400_BAD_REQUEST
            )

        return func(request, *args, **kwargs)
    return validation
