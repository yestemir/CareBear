from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .checkbox import Checkbox


class HealthStatus(models.Model):
    date = models.DateTimeField(
        verbose_name=_('date'), help_text=_('date'),
    )
    mood_percentage = models.IntegerField(
        verbose_name=_('mood_percentage'), help_text=_('mood_percentage'),
        default=0
    )
    mood = models.CharField(
        verbose_name=_('mood'), help_text=_('mood'),
        max_length=100, default=''
    )
    comment = models.CharField(
        verbose_name=_('comment'), help_text=_('comment'),
        max_length=100, default=''
    )
    nutrition = models.ForeignKey(
        to='library.checkbox', on_delete=models.SET_NULL,
        null=True, related_name='nutrition',
        verbose_name=_('task'), help_text=_('task')
    )
    # image = models.FileField(blank=True, upload_to='photos/%d-%m-%Y')
    pills = models.ForeignKey(
        to='library.checkbox', on_delete=models.SET_NULL,
        null=True, related_name='pills',
        verbose_name=_('task'), help_text=_('task')
    )
    todos = models.ForeignKey(
        to='library.checkbox', on_delete=models.SET_NULL,
        null=True, related_name='todos',
        verbose_name=_('task'), help_text=_('task')
    )
    checkboxes = models.ManyToManyField(Checkbox)

    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.SET_NULL,
        null=True, related_name='health_status',
        verbose_name=_('user'), help_text=_('user')
    )
    # nutrition = models.ForeignKey(
    #     to='library.checkbox', on_delete=models.SET_NULL,
    #     null=True, related_name='health_status',
    #     verbose_name=_('task'), help_text=_('task')
    # )
    # image = models.FileField(blank=True, upload_to='photos/%d-%m-%Y')
    # pills = models.ForeignKey(
    #     to='library.checkbox', on_delete=models.SET_NULL,
    #     null=True, related_name='health_status',
    #     verbose_name=_('task'), help_text=_('task')
    # )
    # todos = models.ForeignKey(
    #     to='library.checkbox', on_delete=models.SET_NULL,
    #     null=True, related_name='health_status',
    #     verbose_name=_('task'), help_text=_('task')
    # )
    # custom = models.CharField(
    #     verbose_name=_('isbn'), help_text=_('isbn'),
    #     max_length=100, default=''
    # )

    objects: Manager

    class Meta:
        app_label = 'library'
        db_table = 'library.books'
        verbose_name = _('health_status')
        verbose_name_plural = _('health_status')

    # def __str__(self):
    #     return self.title
