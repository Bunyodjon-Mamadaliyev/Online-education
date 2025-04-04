from django.urls import path
from .views import CourseListCreateView, CourseDetailView, CoursesByCategoryView

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/category/<int:category_id>/', CoursesByCategoryView.as_view(), name='courses-by-category'),
]
