from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext_lazy as _


class Checkboxes(models.Model):
    title = models.CharField(
        verbose_name=_('title'), help_text=_('title'),
        max_length=250, default=''
    )
    checkboxes = models.ManyToManyField(
        to='library.checkbox', related_name='checkboxes',
        verbose_name=_('task'), help_text=_('task')
    )
    # user = models.ForeignKey(
    #     to=get_user_model(), on_delete=models.SET_NULL,
    #     null=True, related_name='saved_books',
    #     verbose_name=_('user'), help_text=_('user')
    # )
    # created = models.DateTimeField(
    #     auto_now_add=True, help_text=_('created'),
    #     verbose_name=_('created'),
    # )

    objects: Manager

    class Meta:
        app_label = 'library'
        db_table = 'library.checkboxes'
        verbose_name = _('checkboxes')
        verbose_name_plural = _('checkboxes')
