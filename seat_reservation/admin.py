from django.contrib import admin

from . import models


@admin.register(models.Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['code', ' is_disabled']
