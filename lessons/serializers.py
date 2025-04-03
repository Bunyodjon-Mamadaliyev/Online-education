from rest_framework import serializers
from .models import Lesson
from modules.models import Module
from modules.serializers import ModuleSerializer

class LessonSerializer(serializers.ModelSerializer):
    module = serializers.PrimaryKeyRelatedField(queryset=Module.objects.all(), write_only=True)
    module_detail = ModuleSerializer(source='module', read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'module', 'module_detail', 'title', 'content', 'video_url', 'duration', 'order', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
