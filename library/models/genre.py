from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext_lazy as _


class Genre(models.Model):
    title = models.CharField(
        verbose_name=_('title'), help_text=_('title'),
        max_length=32
    )

    objects: Manager

    class Meta:
        app_label = 'library'
        db_table = 'library.genres'
        verbose_name = _('genre')
        verbose_name_plural = _('genres')
