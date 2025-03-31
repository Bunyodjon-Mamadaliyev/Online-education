from django.contrib import admin
from .models import Lesson

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'order', 'duration', 'created_at')
    list_filter = ('module', 'created_at')
    search_fields = ('title', 'module__name')
    ordering = ('module', 'order')
    list_editable = ('order',)
