from django.core.exceptions import ValidationError
from django.db import models

from apps.general.validate import phone_number_validate


class General(models.Model):
    class WeekDay(models.IntegerChoices):
        MONDAY = 1, 'Monday'
        TUESDAY = 2, 'Tuesday'
        WEDNESDAY = 3, 'Wednesday'
        THURSDAY = 4, 'Thursday'
        FRIDAY = 5, 'Friday'
        SATURDAY = 6, 'Saturday'
        SUNDAY = 7, 'Sunday'

    logo = models.ImageField(upload_to='general/image/')
    banner = models.ImageField(upload_to='general/banner/')
    video_url =  models.URLField(blank=True, null=True)
    title = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, validators=[phone_number_validate])
    email = models.EmailField()
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    work_start_day = models.IntegerField(choices=WeekDay.choices, default=1)
    work_end_day = models.IntegerField(choices=WeekDay.choices,  default=6)
    work_start_time = models.TimeField()
    work_end_time = models.TimeField()
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)

    def clean(self):
        if self.work_start_day and self.work_end_day:
            if self.work_start_day >= self.work_end_day:
                raise ValidationError('Work start day cannot be greater than or equal to work end day')
        if self.work_start_time and self.work_end_time:
            if self.work_start_time >= self.work_end_time:
                raise ValidationError('Work start time cannot be greater than or equal to work end time')

