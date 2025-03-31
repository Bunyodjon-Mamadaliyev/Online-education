from rest_framework import serializers
from courses.serializers import CourseSerializer
from .models import Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    course = CourseSerializer()

    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course', 'enrolled_at', 'is_completed', 'completed_at']
        read_only_fields = ['enrolled_at', 'completed_at']
