from rest_framework import serializers
from .models import Enrollment
from users.models import User
from courses.models import Course

class EnrollmentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']

class EnrollmentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title']

class EnrollmentSerializer(serializers.ModelSerializer):
    user = EnrollmentUserSerializer()
    course = EnrollmentCourseSerializer()
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source="user")
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), write_only=True, source="course")
    enrolled_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ", read_only=True)
    completed_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ", allow_null=True, read_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course', 'user_id', 'course_id', 'enrolled_at', 'is_completed', 'completed_at']

    def create(self, validated_data):
        enrollment = Enrollment.objects.create(**validated_data)
        return enrollment