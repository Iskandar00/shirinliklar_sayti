from django.db import models

from apps.general.validate import phone_number_validate


class Order(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, validators=[phone_number_validate])
    product_name = models.CharField(max_length=100)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}-{self.name}"
