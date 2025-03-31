from rest_framework import serializers
from .models import Lesson
from modules.serializers import ModuleSerializer

class LessonSerializer(serializers.ModelSerializer):
    module = ModuleSerializer()

    class Meta:
        model = Lesson
        fields = ['id', 'module', 'title', 'content', 'video_url', 'duration', 'order', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
