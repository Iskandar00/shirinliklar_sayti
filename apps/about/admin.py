from django.contrib import admin

from apps.about.models import About
from apps.about.models import CustomerOpinion

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'slug', 'name_ru', 'created_at', 'updated_at', 'ordering_number',)
    list_display_links = list_display
    search_fields = ('name_uz', 'name_ru', 'slug',)
    prepopulated_fields = {'slug': ('name_uz',)}
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'ordering_number',)


@admin.register(CustomerOpinion)
class CustomerOpinionAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'name_ru', 'created_at')
    list_display_links = list_display
    search_fields = ('name_uz', 'name_ru',)
    list_filter = ('created_at',)
