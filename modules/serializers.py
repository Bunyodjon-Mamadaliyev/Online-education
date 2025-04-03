from rest_framework import serializers
from courses.models import Course
from .models import Module

class ModuleSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    class Meta:
        model = Module
        fields = ['id', 'course', 'title', 'description', 'order', 'created_at']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        return Module.objects.create(**validated_data)
