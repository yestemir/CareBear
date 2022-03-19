from django.contrib import admin

from library.models import HealthStatus, Checkbox, Checkboxes

admin.site.register(HealthStatus)
admin.site.register(Checkbox)
admin.site.register(Checkboxes)
