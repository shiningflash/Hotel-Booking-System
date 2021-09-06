from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import BaseModel
from room.models import Room


class Booking(BaseModel):
    customer_phone_no      = models.CharField(verbose_name='phone_no', max_length=100)
    room                   = models.ForeignKey(Room, on_delete=models.CASCADE)
    price                  = models.FloatField(default=0.0)
    discounted_price       = models.FloatField(default=0.0)
    booking_time           = models.DateTimeField(verbose_name='last reservation time')
    booking_start_time     = models.DateTimeField(verbose_name='booking start time')
    booking_end_time       = models.DateTimeField(verbose_name='booking end time')
    last_checkin_time      = models.DateTimeField(verbose_name='last checkin time', null=True, blank=True)
    last_checkout_time     = models.DateTimeField(verbose_name='last checkout time', null=True, blank=True)

    def __str__(self):
        return f'{self.customer_phone_no}'

    class Meta:
        ordering = ['-created_at']
        db_table = 'bookings'
        verbose_name = _('Booking')
        verbose_name_plural = _('Bookings')
        indexes = [
            models.Index(fields=['customer_phone_no']),
            models.Index(fields=['room'])
        ]
