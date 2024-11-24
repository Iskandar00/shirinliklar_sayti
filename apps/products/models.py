from django.core.exceptions import ValidationError
from django.db import models

from apps.general.validate import field_language


class Product(models.Model):
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='products')

    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)

    image = models.ImageField(upload_to='products/image')

    description_uz = models.CharField(max_length=700)
    description_ru = models.CharField(max_length=700)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    unique_together = ('category', 'name_uz')

    @property
    def name(self):
        return field_language(self, 'name')

    @property
    def description(self):
        return field_language(self, 'description')

    def clean(self):
        if self.category.products:
            if self.category.products.count() >= 6 and not self.pk:
                raise ValidationError(
                    f"You cannot add more than 6 products to the category '{self.category.name_uz}'."
                )

    def __str__(self):
        return self.name_uz


class AdditionalAdvertising(models.Model):
    name_uz = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    name_ru = models.CharField(max_length=255)

    image = models.ImageField(upload_to='products/image')

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    description_uz = models.CharField(max_length=700)
    description_ru = models.CharField(max_length=700)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def name(self):
        return field_language(self, 'name')

    @property
    def description(self):
        return field_language(self, 'description')

    def __str__(self):
        return self.name_uz
