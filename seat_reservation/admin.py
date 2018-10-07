from django.contrib import admin

from . import models


@admin.register(models.Seat)
class SeatAdmin(admin.ModelAdmin):
    pass
