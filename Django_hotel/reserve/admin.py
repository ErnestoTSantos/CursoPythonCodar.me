from django.contrib import admin

from reserve.models import Reserve


@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    ...
