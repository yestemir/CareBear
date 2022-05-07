from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext_lazy as _


class Test(models.Model):
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.SET_NULL,
        null=True, related_name='test',
        verbose_name=_('user'), help_text=_('user')
    )
    # test_results = models.ForeignKey(
    #     to='library.test_results', related_name='test',
    #     on_delete=models.SET_NULL, null=True,
    #     verbose_name=_('test_results'), help_text=_('test_results'),
    # )
    # test_attempts = models.ForeignKey(
    #     to='library.test_attempts', related_name='test',
    #     on_delete=models.SET_NULL, null=True,
    #     verbose_name=_('test_attempts'), help_text=_('test_attempts'),
    # )
    # questions = models.CharField(
    #     verbose_name=_('test'), help_text=_('test'),
    #     max_length=1000, default='', blank=True
    # )
    # created = models.DateTimeField(
    #     auto_now_add=True, help_text=_('created'),
    #     verbose_name=_('created'),
    # )

    objects: Manager

    class Meta:
        app_label = 'library'
        db_table = 'library.test'
        verbose_name = _('test')
        verbose_name_plural = _('test')
