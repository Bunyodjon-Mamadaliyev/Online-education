from rest_framework import serializers
from categories.serializers import CategorySerializer
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    teacher = serializers.StringRelatedField()
    final_price = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'teacher', 'category', 'price', 'discount_price', 'final_price', 'image', 'is_published', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def get_final_price(self, obj):
        return obj.discount_price if obj.discount_price else obj.price