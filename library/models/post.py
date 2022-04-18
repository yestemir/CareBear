from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    text = models.CharField(
        verbose_name=_('comment'), help_text=_('comment'),
        max_length=1000, default='', blank=True, null=True
    )
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.SET_NULL,
        null=True, related_name='post',
        verbose_name=_('user'), help_text=_('user')
    )
    # username = models.ForeignKey(
    #     to=get_user_model(), on_delete=models.SET_NULL,
    #     null=True, related_name='post',
    #     verbose_name=_('username'), help_text=_('username')
    # )
    created = models.DateTimeField(
        auto_now_add=True, help_text=_('created_at'),
        verbose_name=_('created_at'),
    )

    objects: Manager

    class Meta:
        app_label = 'library'
        db_table = 'library.post'
        verbose_name = _('post')
        verbose_name_plural = _('post')
