from rest_framework import serializers
from .models import Progress

class ProgressSerializer(serializers.ModelSerializer):
    enrollment = serializers.StringRelatedField()
    lesson = serializers.StringRelatedField()

    class Meta:
        model = Progress
        fields = ['id', 'enrollment', 'lesson', 'is_completed', 'completed_at']
        read_only_fields = ['completed_at']