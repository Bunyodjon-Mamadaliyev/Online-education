from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Enrollment
from .serializers import EnrollmentSerializer
from common.pagination import DefaultPagination

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all().order_by('-enrolled_at')
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagination


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserEnrollmentsView(generics.ListAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagination

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Enrollment.objects.filter(user_id=user_id)

class CourseEnrollmentsView(generics.ListAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagination

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        return Enrollment.objects.filter(course_id=course_id)
