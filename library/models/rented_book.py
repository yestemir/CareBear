# from django.contrib.auth import get_user_model
# from django.db import models
# from django.db.models import Manager
# from django.utils.translation import gettext_lazy as _
#
#
# class RentedBook(models.Model):
#     book = models.ForeignKey(
#         to='library.Book', on_delete=models.SET_NULL,
#         null=True, related_name='rented_books',
#         verbose_name=_('book'), help_text=_('book')
#     )
#     user = models.ForeignKey(
#         to=get_user_model(), on_delete=models.SET_NULL,
#         null=True, related_name='rented_books',
#         verbose_name=_('user'), help_text=_('user')
#     )
#     created = models.DateTimeField(
#         auto_now_add=True, help_text=_('created'),
#         verbose_name=_('created'),
#     )
#     state = models.CharField(
#         verbose_name=_('state'), help_text=_('state'),
#         max_length=32, default='reading'
#     )
#     term = models.IntegerField(
#         verbose_name=_('term'), help_text=_('term'),
#         default=0
#     )
#
#     objects: Manager
#
#     class Meta:
#         app_label = 'library'
#         db_table = 'library.rented_books'
#         verbose_name = _('rented_book')
#         verbose_name_plural = _('rented_books')
