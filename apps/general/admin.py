from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import General


@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'phone_number', 'email', 'city', 'address',
        'banner',  'video_url', 'logo',
        'work_start_day', 'work_end_day', 'work_start_time',
        'work_end_time', 'longitude', 'latitude'
    )
    list_display_links = list_display

    def save_model(self, request, obj, form, change):
        if not change and General.objects.exists():
            raise ValidationError('Faqat bitta General obyektiga ruxsat berilgan.')
        super().save_model(request, obj, form, change)
