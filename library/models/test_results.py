from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


class TestResults(models.Model):
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.SET_NULL,
        null=True, related_name='test_results',
        verbose_name=_('user'), help_text=_('user')
    )
    min_result = models.IntegerField(
        verbose_name=_('min_result'), help_text=_('min_result'),
        default=0, blank=True, validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    max_result = models.IntegerField(
        verbose_name=_('max_result'), help_text=_('max_result'),
        default=0, blank=True, validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    test = models.ForeignKey(
        to='library.test', related_name='test_results',
        on_delete=models.SET_NULL, null=True,
        verbose_name=_('test'), help_text=_('test'),
    )
    title = models.CharField(
        verbose_name=_('test_results'), help_text=_('test_results'),
        max_length=1000, default='', blank=True
    )

    objects: Manager

    class Meta:
        app_label = 'library'
        db_table = 'library.test_results'
        verbose_name = _('test_results')
        verbose_name_plural = _('test_results')
