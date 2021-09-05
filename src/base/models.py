from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.CharField(null=False, blank=False, max_length=150)
    updated_by = models.CharField(null=False, blank=False, max_length=150)

    class Meta:
        abstract = True
        app_label = 'base'
