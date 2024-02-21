import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Base(models.Model):
    active = models.BooleanField(
        verbose_name=_('ativo'),
        default=True,
        help_text=_('ativar ou desativar este item.'),
    )
    created_at = models.DateTimeField(
        verbose_name=_('criado em'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('atualizado em'),
        auto_now=True,
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True
