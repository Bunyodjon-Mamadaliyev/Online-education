from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from .models import Progress
from .serializers import ProgressSerializer
from rest_framework.permissions import IsAuthenticated

class ProgressViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def get_queryset(self):
        # Filter based on the URL parameter
        if 'enrollment_id' in self.kwargs:
            return Progress.objects.filter(enrollment__id=self.kwargs['enrollment_id'])
        return Progress.objects.all()

    @action(detail=False, methods=['get'], url_path='enrollment/(?P<enrollment_id>\d+)')
    def progress_by_enrollment(self, request, enrollment_id=None):
        """
        Custom action to get progress by enrollment ID.
        """
        progress = self.get_queryset()
        serializer = self.get_serializer(progress, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Custom create method to handle progress creation.
        """
        data = request.data
        enrollment = data.get('enrollment')
        lesson = data.get('lesson')

        # Ensure the enrollment and lesson are valid (optional, you can add custom validation if needed)
        if not enrollment or not lesson:
            return Response({'detail': 'Enrollment and lesson are required fields.'},
                            status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Custom update method to handle progress updates.
        """
        # You can add any custom logic before updating
        return super().update(request, *args, **kwargs)

