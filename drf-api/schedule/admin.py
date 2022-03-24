from django.contrib import admin

from .models import Faithfulness, Scheduling


@admin.register(Scheduling)
class SchedulingAdmin(admin.ModelAdmin):
    list_display = ('provider', 'client_name', 'client_email', 'client_phone', 'date_time', 'states', 'confirmed', 'canceled',)  # noqa:E501


@admin.register(Faithfulness)
class FaithfulnessAdmin(admin.ModelAdmin):
    list_display = ('provider', 'client', 'level')
