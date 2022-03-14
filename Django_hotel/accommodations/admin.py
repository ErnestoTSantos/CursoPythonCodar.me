from django.contrib import admin

from accommodations.models import Accommodation, Company


@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    ...


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    ...
