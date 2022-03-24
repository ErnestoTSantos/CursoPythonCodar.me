from django.contrib import admin

from .models import Scheduling


@admin.register(Scheduling)
class SchedulingAdmin(admin.ModelAdmin):
    list_display = ('provider', 'client_name', 'client_email',
                    'client_phone', 'date_time', 'canceled')
