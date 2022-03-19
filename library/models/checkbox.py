from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext_lazy as _


class Checkbox(models.Model):
    task = models.CharField(
        verbose_name=_('task'), help_text=_('task'),
        max_length=100
    )
    done = models.BooleanField(
        verbose_name=_('done'), help_text=_('done'),
        default=False
    )
    everyday = models.BooleanField(
        verbose_name=_('everyday'), help_text=_('everyday'),
        default=False
    )

    objects: Manager

    class Meta:
        app_label = 'library'
        db_table = 'library.genres'
        verbose_name = _('checkbox')
        verbose_name_plural = _('checkbox')

    # def __str__(self):
    #     return self.title
