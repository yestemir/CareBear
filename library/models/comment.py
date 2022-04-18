from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext_lazy as _


class Comment(models.Model):
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.SET_NULL,
        null=True, related_name='comment',
        verbose_name=_('user'), help_text=_('user')
    )
    post = models.ForeignKey(
        to='library.post', related_name='comment',
        on_delete=models.SET_NULL, null=True,
        verbose_name=_('post'), help_text=_('post'),
    )
    text = models.CharField(
        verbose_name=_('comment'), help_text=_('comment'),
        max_length=1000, default='', blank=True
    )
    created = models.DateTimeField(
        auto_now_add=True, help_text=_('created'),
        verbose_name=_('created'),
    )

    objects: Manager

    class Meta:
        app_label = 'library'
        db_table = 'library.comment'
        verbose_name = _('comment')
        verbose_name_plural = _('comment')
