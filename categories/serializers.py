from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'icon', 'products_count',
                  'subcategories', 'created_at']
        read_only_fields = ['created_at']

    def get_products_count(self, obj):
        return obj.products.count() if hasattr(obj, 'products') else 0

    def get_subcategories(self, obj):
        return CategorySerializer(obj.subcategories.all(), many=True, context=self.context).data
