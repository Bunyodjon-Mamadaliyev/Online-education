from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'icon', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
