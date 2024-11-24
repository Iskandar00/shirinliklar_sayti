from django.core.exceptions import ValidationError
from django.db import models

from apps.general.validate import field_language


class About(models.Model):
    name_uz = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    name_ru = models.CharField(max_length=100)

    description_uz = models.TextField(max_length=2000)
    description_ru = models.TextField(max_length=2000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ordering_number = models.PositiveSmallIntegerField(default=1)

    @property
    def name(self):
        return field_language(self, 'name')

    @property
    def description(self):
        return field_language(self, 'description')

    def clean(self):
        if About.objects.count() >= 4 and not self.pk:
            raise ValidationError("You cannot create more than 4 about.")

    def save(self, *args, **kwargs):
        if not self.pk:
            existing_count = About.objects.count()
            if existing_count < 4:
                self.ordering_number = existing_count + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_uz


class CustomerOpinion(models.Model):
    name_uz = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)

    description_uz = models.TextField(max_length=2000)
    description_ru = models.TextField(max_length=2000)


    image = models.ImageField(upload_to='customer_image', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def name(self):
        return field_language(self, 'name')

    @property
    def description(self):
        return field_language(self, 'description')

    def __str__(self):
        return self.name_uz