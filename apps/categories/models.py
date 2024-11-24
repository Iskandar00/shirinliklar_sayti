from django.db import models
from django.core.exceptions import ValidationError

from apps.general.validate import field_language


class Category(models.Model):
    name_uz = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    name_ru = models.CharField(max_length=100)
    ordering_number = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def name(self):
        return field_language(self, 'name')

    def clean(self):
        if Category.objects.count() >= 4 and not self.pk:
            raise ValidationError("You cannot create more than 4 categories.")

    def save(self, *args, **kwargs):
        if not self.pk:
            existing_count = Category.objects.count()
            if existing_count < 4:
                self.ordering_number = existing_count + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_uz
