from rest_framework import generics, permissions
from .models import Course
from .serializers import CourseSerializer
from common.pagination import DefaultPagination

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = DefaultPagination

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CoursesByCategoryView(generics.ListAPIView):
    serializer_class = CourseSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Course.objects.filter(category_id=category_id)
