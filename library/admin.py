from django.contrib import admin

from library.models import HealthStatus, Checkbox, Post, Comment, Badge, \
    UserBadge, Test

admin.site.register(HealthStatus)
admin.site.register(Checkbox)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Badge)
admin.site.register(UserBadge)
admin.site.register(Test)
