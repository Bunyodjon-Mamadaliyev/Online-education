from rest_framework import serializers
from .models import Progress
from enrollments.models import Enrollment
from lessons.models import Lesson

# Serializer for the Enrollment model
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'course']

# Serializer for the Lesson model
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title']

# Serializer for the Progress model
class ProgressSerializer(serializers.ModelSerializer):
    enrollment = EnrollmentSerializer()
    lesson = LessonSerializer()

    class Meta:
        model = Progress
        fields = ['id', 'enrollment', 'lesson', 'is_completed', 'completed_at']
