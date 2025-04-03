from rest_framework import generics
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Module
from .serializers import ModuleSerializer
from courses.models import Course
from common.pagination import DefaultPagination

class ModuleListCreateView(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    pagination_class = DefaultPagination

class ModuleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

@api_view(['GET'])
def modules_by_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    modules = Module.objects.filter(course=course).order_by('order')
    paginator = DefaultPagination()
    result_page = paginator.paginate_queryset(modules, request)
    serializer = ModuleSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
