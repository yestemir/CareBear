from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    title = models.CharField(
        verbose_name=_('title'), help_text=_('title'),
        max_length=32
    )
    description = models.TextField(
        verbose_name=_('description'), help_text=_('description'),
        default=''
    )
    author = models.CharField(
        verbose_name=_('author'), help_text=_('author'),
        max_length=32, default=''
    )
    rating = models.DecimalField(
        verbose_name=_('rating'), help_text=_('rating'),
        default=0, decimal_places=1, max_digits=3
    )
    genre = models.ForeignKey(
        to='library.Genre', on_delete=models.SET_NULL,
        null=True, related_name='books',
        verbose_name=_('genre'), help_text=_('genre')
    )
    image = models.FileField(blank=True, upload_to='photos/%d-%m-%Y')
    created = models.DateTimeField(
        verbose_name=_('created'), help_text=_('created'),
        auto_now_add=True,
    )
    release_date = models.DateTimeField(
        verbose_name=_('release_date'), help_text=_('release_date'),
    )
    isbn = models.CharField(
        verbose_name=_('isbn'), help_text=_('isbn'),
        max_length=32, default=''
    )
    quantity = models.IntegerField(
        verbose_name=_('quantity'), help_text=_('quantity'),
        default=0
    )
    language = models.CharField(
        verbose_name=_('language'), help_text=_('language'),
        max_length=32, default='russian'
    )
    link = models.CharField(
        verbose_name=_('link'), help_text=_('link'),
        max_length=200, default='', null=True
    )

    objects: Manager

    class Meta:
        app_label = 'library'
        db_table = 'library.books'
        verbose_name = _('book')
        verbose_name_plural = _('books')
