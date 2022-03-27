import calendar

from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class HealthStatus(models.Model):
    date = models.DateField(
        verbose_name=_('date'), help_text=_('date'),
        default=datetime.date.today(), blank=True,
    )
    def date_trunc_field(self):
        return self.date_field.date()

    mood_percentage = models.IntegerField(
        verbose_name=_('mood_percentage'), help_text=_('mood_percentage'),
        default=0, blank=True, validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    mood = models.CharField(
        verbose_name=_('mood'), help_text=_('mood'),
        max_length=100, default='', blank=True
    )
    comment = models.CharField(
        verbose_name=_('comment'), help_text=_('comment'),
        max_length=250, default='', blank=True
    )
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.SET_NULL,
        null=True, related_name='health_status',
        verbose_name=_('user'), help_text=_('user')
    )
    # image = models.FileField(blank=True, upload_to='photos/%d-%m-%Y')

    objects: Manager

    class Meta:
        app_label = 'library'
        db_table = 'library.books'
        verbose_name = _('health_status')
        verbose_name_plural = _('health_status')

    # def __str__(self):
    #     return self.title
