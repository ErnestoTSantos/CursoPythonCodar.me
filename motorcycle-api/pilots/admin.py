from django.contrib import admin

from .models import Pilot


@admin.register(Pilot)
class PilotAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "age",
        "number",
        "automaker",
        "championships_won",
        "retired",
    )  # noqa:E501
