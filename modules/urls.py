from django.urls import path
from .views import ModuleListCreateView, ModuleDetailView, modules_by_course

urlpatterns = [
    path('modules/', ModuleListCreateView.as_view(), name='module-list'),
    path('modules/<int:pk>/', ModuleDetailView.as_view(), name='module-detail'),
    path('modules/course/<int:course_id>/', modules_by_course, name='modules-by-course'),
]
