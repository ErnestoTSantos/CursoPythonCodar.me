from django.contrib import admin

from schedule.models import Category, Event

admin.site.register(Event)
admin.site.register(Category)
