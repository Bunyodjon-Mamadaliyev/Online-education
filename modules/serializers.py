from rest_framework import serializers
from .models import Module

class ModuleSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField()

    class Meta:
        model = Module
        fields = ['id', 'course', 'title', 'description', 'order', 'created_at']
        read_only_fields = ['created_at']