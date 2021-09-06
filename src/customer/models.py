from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import BaseModel


class Customer(BaseModel):
    class Gender(models.TextChoices):
        MALE = 'male', _('male')
        FEMALE = 'female', _('female')
        OTHERS = 'others', _('others')

    phone_no         = models.CharField(verbose_name='phone_no', max_length=100, unique=True)
    first_name       = models.CharField(max_length=100)
    last_name        = models.CharField(max_length=100)
    email            = models.EmailField(verbose_name='email', max_length=100, null=True, blank=True)
    gender           = models.CharField(max_length=10, choices=Gender.choices, default=Gender.MALE)
    occupation       = models.CharField(max_length=100, null=True, blank=True)
    country          = models.CharField(max_length=100, null=True, blank=True)
    address          = models.CharField(max_length=100, null=True, blank=True)
    details          = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.email} - {self.phone_no}'

    class Meta:
        ordering = ['-created_at']
        db_table = 'customers'
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
        indexes = [
            models.Index(fields=['phone_no']),
            models.Index(fields=['first_name']),
            models.Index(fields=['email']),
            models.Index(fields=['country']),
            models.Index(fields=['occupation']),
            models.Index(fields=['gender'])
        ]
