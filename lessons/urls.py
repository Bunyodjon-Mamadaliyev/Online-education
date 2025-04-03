from django.urls import path
from .views import LessonListCreateView, LessonDetailView, LessonByModuleView

urlpatterns = [
    path('lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('lessons/module/<int:module_id>/', LessonByModuleView.as_view(), name='lesson-by-module'),
]
