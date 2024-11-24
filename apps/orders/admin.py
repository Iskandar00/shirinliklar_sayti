from django.contrib import admin
from apps.orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'product_name', 'address', 'created_at')
    list_display_links = list_display
    search_fields = ('name', 'phone_number', 'product_name', 'address')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
