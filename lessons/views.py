from rest_framework import generics
from .models import Lesson
from .serializers import LessonSerializer
from modules.models import Module
from common.pagination import DefaultPagination

class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = DefaultPagination

    def perform_create(self, serializer):
        module_id = self.request.data.get('module')
        if module_id:
            try:
                module = Module.objects.get(id=module_id)
                serializer.save(module=module)
            except Module.DoesNotExist:
                raise Exception(f"Module with id {module_id} does not exist.")
        else:
            raise Exception("Module ID must be provided.")

class LessonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonByModuleView(generics.ListAPIView):
    serializer_class = LessonSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        module_id = self.kwargs['module_id']
        try:
            module = Module.objects.get(id=module_id)
            return Lesson.objects.filter(module=module)
        except Module.DoesNotExist:
            return Lesson.objects.none()
