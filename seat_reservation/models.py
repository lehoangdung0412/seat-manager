from django.db import models


class Seat(models.Model):
    code = models.CharField(max_length=255)
    is_disabled = models.BooleanField(default=False)

    def __str__(self):
        if self.is_disabled:
            return '{} (Disabled)'.format(self.code)
        return self.code

