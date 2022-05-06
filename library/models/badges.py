from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext_lazy as _


class Badge(models.Model):
    name = models.CharField(
        verbose_name=_('name'), help_text=_('name'),
        max_length=250, default=''
    )
    description = models.CharField(
        verbose_name=_('description'), help_text=_('description'),
        max_length=250, default=''
    )

    objects: Manager

    class Meta:
        app_label = 'library'
        db_table = 'library.badges'
        verbose_name = _('badge')
        verbose_name_plural = _('badge')
