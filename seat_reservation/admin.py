from django.contrib import admin

from . import models


@admin.register(models.Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['code', 'is_disabled']


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass
