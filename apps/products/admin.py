from django.contrib import admin
from apps.products.models import Product
from apps.products.models import AdditionalAdvertising


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'name_ru', 'category', 'price', 'created_at', 'updated_at')
    list_display_links = list_display
    readonly_fields = ('created_at', 'updated_at',)
    search_fields = ('name_uz', 'name_ru', 'description')
    list_filter = ('category', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    list_select_related = ('category',)



@admin.register(AdditionalAdvertising)
class AdditionalAdvertisingAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'name_ru', 'slug', 'price', 'created_at', 'updated_at')
    list_display_links = list_display
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name_uz', 'name_ru', 'slug',)
    list_filter = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name_uz',)}