from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from reviews.models import Review
from .serializers import ReviewSerializer
from common.pagination import DefaultPagination

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = DefaultPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

