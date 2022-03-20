from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class Checkbox(models.Model):
    name = models.CharField(
        verbose_name=_('name'), help_text=_('name'),
        max_length=250, default=''
    )
    title = models.CharField(
        verbose_name=_('title'), help_text=_('title'),
        max_length=250, default=''
    )
    done = models.BooleanField(
        verbose_name=_('done'), help_text=_('done'),
        default=False
    )
    everyday = models.BooleanField(
        verbose_name=_('everyday'), help_text=_('everyday'),
        default=False
    )
    type = models.CharField(
        verbose_name=_('type'), help_text=_('type'),
        max_length=250, default=''
    )
    health_status = models.ForeignKey(
        to='library.HealthStatus', on_delete=models.SET_NULL,
        null=True, related_name='checkbox',
        verbose_name=_('health_status'), help_text=_('health_status')
    )
    user_id = models.ForeignKey(
        to=get_user_model(), on_delete=models.SET_NULL,
        null=True, related_name='checkbox',
        verbose_name=_('user_id'), help_text=_('user_id')
    )

    objects: Manager

    class Meta:
        app_label = 'library'
        db_table = 'library.genres'
        verbose_name = _('checkbox')
        verbose_name_plural = _('checkbox')

    # def __str__(self):
    #     return self.title
