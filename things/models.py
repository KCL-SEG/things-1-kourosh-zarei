from django.db import models
from django.db.models import Model
from django.core.exceptions import ValidationError


class Thing(Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

    def clean(self):
        if self.quantity < 0 or self.quantity > 100:
            raise ValidationError("Quantity must be between 0 and 100")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
