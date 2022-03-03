from django.contrib import admin

from to_do_list.models import Chore


@admin.register(Chore)
class ChoreAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'active', 'create_date',
                    'update_date', 'final_date')
