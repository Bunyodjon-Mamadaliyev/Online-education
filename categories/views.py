from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Category
from .serializers import CategorySerializer
from common.pagination import DefaultPagination

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = DefaultPagination

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]