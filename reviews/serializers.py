from rest_framework import serializers
from .models import Review
from courses.models import Course
from users.serializers import UserSerializer

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    class Meta:
        model = Review
        fields = ["id", "user", "course", "rating", "comment", "created_at", "updated_at"]
