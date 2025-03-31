from django.contrib import admin
from .models import Enrollment

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_at', 'is_completed', 'completed_at')
    list_filter = ('is_completed', 'enrolled_at')
    search_fields = ('user__username', 'course__title')
    ordering = ('-enrolled_at',)
    list_editable = ('is_completed',)
