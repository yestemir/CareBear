# from django.contrib.auth import get_user_model
# from django.db import models
# from django.db.models import Manager
# from django.utils.translation import gettext_lazy as _
#
#
# class Review(models.Model):
#     book = models.ForeignKey(
#         to='library.Book', on_delete=models.SET_NULL,
#         null=True, related_name='reviews',
#         verbose_name=_('book'), help_text=_('book')
#     )
#     user = models.ForeignKey(
#         to=get_user_model(), on_delete=models.SET_NULL,
#         null=True, related_name='reviews',
#         verbose_name=_('user'), help_text=_('user')
#     )
#     created = models.DateTimeField(
#         auto_now_add=True, help_text=_('created_at'),
#         verbose_name=_('created_at'),
#     )
#     text = models.TextField(
#         verbose_name=_('text'), help_text=_('text'),
#     )
#     rating = models.DecimalField(
#         verbose_name=_('rating'), help_text=_('rating'),
#         default=0, decimal_places=1, max_digits=1
#     )
#
#     objects: Manager
#
#     class Meta:
#         app_label = 'library'
#         db_table = 'library.reviews'
#         verbose_name = _('review')
#         verbose_name_plural = _('reviews')
