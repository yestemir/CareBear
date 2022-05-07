from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class TestAttempts(models.Model):
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.SET_NULL,
        null=True, related_name='test_attempts',
        verbose_name=_('user'), help_text=_('user')
    )
    result = models.IntegerField(
        verbose_name=_('result'), help_text=_('result'),
        default=0, blank=True, validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    date = models.DateTimeField(
        auto_now_add=True, help_text=_('date'),
        verbose_name=_('date'),
    )
    test = models.ForeignKey(
        to='library.test', related_name='test_attempts',
        on_delete=models.SET_NULL, null=True,
        verbose_name=_('test'), help_text=_('test'),
    )

    objects: Manager

    class Meta:
        app_label = 'library'
        db_table = 'library.test_attempt'
        verbose_name = _('test_attempt')
        verbose_name_plural = _('test_attempt')
