from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext_lazy as _


class SavedBook(models.Model):
    book = models.ForeignKey(
        to='library.Book', on_delete=models.SET_NULL,
        null=True, related_name='saved_books',
        verbose_name=_('book'), help_text=_('book')
    )
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.SET_NULL,
        null=True, related_name='saved_books',
        verbose_name=_('user'), help_text=_('user')
    )
    created = models.DateTimeField(
        auto_now_add=True, help_text=_('created'),
        verbose_name=_('created'),
    )

    objects: Manager

    class Meta:
        app_label = 'library'
        db_table = 'library.saved_books'
        verbose_name = _('saved_book')
        verbose_name_plural = _('saved_books')
