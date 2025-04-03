from django.urls import path
from .views import UserEnrollmentsView, CourseEnrollmentsView


urlpatterns = [
    path('enrollments/user/<int:user_id>/', UserEnrollmentsView.as_view(), name='user-enrollments'),
    path('enrollments/course/<int:course_id>/', CourseEnrollmentsView.as_view(), name='course-enrollments'),
]
