from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import BaseModel

class Room(BaseModel):
    room_no        = models.CharField(verbose_name='phone_no', max_length=100, unique=True)
    floor_no       = models.IntegerField()
    availability   = models.BooleanField(default=True)
    bed_count      = models.IntegerField()
    price          = models.FloatField()
    details        = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.room_no

    class Meta:
        ordering = ['-created_at']
        db_table = 'rooms'
        verbose_name = _('Room')
        verbose_name_plural = _('Rooms')
        indexes = [
            models.Index(fields=['room_no']),
            models.Index(fields=['floor_no']),
            models.Index(fields=['availability']),
            models.Index(fields=['bed_count'])
        ]