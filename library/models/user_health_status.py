# from django.contrib.auth import get_user_model
# from django.db import models
# from django.db.models import Manager
# from django.utils.translation import gettext_lazy as _
#
#
# class UserHealthStatus(models.Model):
#     user = models.ForeignKey(
#         to=get_user_model(), on_delete=models.SET_NULL, related_name='rented_books',
#         verbose_name=_('user'), help_text=_('user')
#     )
#     health_status = models.ForeignKey(
#         to='library.health_status', related_name='health_status',
#         verbose_name=_('health_status'), help_text=_('health_status'),
#     )
#     # book = models.ForeignKey(
#     #     to='library.Book', on_delete=models.SET_NULL,
#     #     null=True, related_name='rented_books',
#     #     verbose_name=_('book'), help_text=_('book')
#     # )
#     # created = models.DateTimeField(
#     #     auto_now_add=True, help_text=_('created'),
#     #     verbose_name=_('created'),
#     # )
#     # state = models.CharField(
#     #     verbose_name=_('state'), help_text=_('state'),
#     #     max_length=32, default='reading'
#     # )
#     # term = models.IntegerField(
#     #     verbose_name=_('term'), help_text=_('term'),
#     #     default=0
#     # )
#
#     objects: Manager
#
#     class Meta:
#         app_label = 'library'
#         db_table = 'library.user_health_status'
#         verbose_name = _('user_health_status')
#         verbose_name_plural = _('user_health_status')
