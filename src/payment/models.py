from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import BaseModel
from booking.models import Booking


class Payment(BaseModel):
    class Payment_Method_Choices(models.TextChoices):
        CASH = 'cash', _('cash')
        BKASH = 'bkash', _('bkash')
        NAGAD = 'nagad', _('nagad')
        UPAY = 'upay', _('upay')
        CARD = 'card', _('card')
        OTHERS = 'others', _('others')

    booking            = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount             = models.FloatField(default=0.0)
    payment_method     = models.CharField(max_length=100, choices=Payment_Method_Choices.choices, default=Payment_Method_Choices.CASH)

    def __str__(self):
        return f'{self.booking} - {self.amount}'

    class Meta:
        ordering = ['-created_at']
        db_table = 'payments'
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')
        indexes = [
            models.Index(fields=['booking']),
            models.Index(fields=['payment_method'])
        ]
