from django.contrib import admin

from library.models import HealthStatus, Checkbox, Post, Comment

admin.site.register(HealthStatus)
admin.site.register(Checkbox)
admin.site.register(Post)
admin.site.register(Comment)
