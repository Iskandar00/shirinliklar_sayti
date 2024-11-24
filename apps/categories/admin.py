from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'name_ru', 'slug', 'ordering_number', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'ordering_number',)
    list_display_links = list_display
    search_fields = ('name_uz', 'name_ru', 'slug')
    prepopulated_fields = {'slug': ('name_uz',)}
