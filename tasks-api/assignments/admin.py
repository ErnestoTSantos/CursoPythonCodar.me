from django.contrib import admin

from assignments.models import Assignment


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("creator", "task_name", "create_day", "final_day", "active")
