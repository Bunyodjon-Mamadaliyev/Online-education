from django.urls import path, include
from rest_framework.routers import DefaultRouter
from progresses.views import ProgressViewSet
from categories.views import CategoryViewSet
from enrollments.views import EnrollmentViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'progress', ProgressViewSet)
router.register(r'enrollments', EnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
