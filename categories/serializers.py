from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'icon', 'created_at']
        read_only_fields = ['created_at']

    def get_products_count(self, obj):
        return obj.products.count() if hasattr(obj, 'products') else 0


