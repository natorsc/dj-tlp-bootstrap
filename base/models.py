import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class Base(models.Model):
    active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
        help_text=_('activate the item?'),
    )
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True
