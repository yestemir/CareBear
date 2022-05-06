from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class UserBadge(models.Model):
    badge = models.CharField(
        to='library.Badge', on_delete=models.SET_NULL,
        null=True, related_name='user_badge',
        verbose_name=_('badge'), help_text=_('badge')
    )
    have_seen = models.BooleanField(
        verbose_name=_('have_seen'), help_text=_('have_seen'),
        default=False
    )
    current_days_steak = models.IntegerField(
        verbose_name=_('current_days_steak'), help_text=_('current_days_steak'),
        default=0,
    )
    current_perfect_days_steak = models.IntegerField(
        verbose_name=_('current_perfect_days_steak'), help_text=_('current_perfect_days_steak'),
        default=0,
    )
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.SET_NULL,
        null=True, related_name='user_badge',
        verbose_name=_('user'), help_text=_('user')
    )

    objects: Manager

    class Meta:
        app_label = 'library'
        db_table = 'library.user_badges'
        verbose_name = _('user_badge')
        verbose_name_plural = _('user_badge')
