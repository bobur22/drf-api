from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from school.models import StudentModel, CourseModel, ModuleModel, GradesModel, AttendanceLogModel, ClassModel
from .serializers import StudentModelSerializer, CourseModelSerializer, ModuleModelSerializer, GradesModelSerializer, \
    ClassModelSerializer, AttendanceLogSerializer

from rest_framework.viewsets import ViewSet, ReadOnlyModelViewSet, ModelViewSet, GenericViewSet
from rest_framework.decorators import action

class StudentViewSet(ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer

class ModuleViewSet(ModelViewSet):
    queryset = ModuleModel.objects.all()
    serializer_class = ModuleModelSerializer

    @action(methods=['get'], detail=True, url_path='student')
    def get_students(self, request, pk=None):
        if pk:
            students = StudentModel.objects.filter(id=pk).select_related('module_students').first()
            serializer = StudentModelSerializer(students.module_students)
            return Response(serializer.data)
        return Response({'status': 'error', 'message': 'pk none'})



















# class StudentList(generics.ListCreateAPIView):
#     queryset = StudentModel.objects.all()
#     serializer_class = StudentModelSerializer
#
#
# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = StudentModel.objects
#     serializer_class = StudentModelSerializer
#
# class CourseList(generics.ListCreateAPIView):
#     queryset = CourseModel.objects
#     serializer_class = CourseModelSerializer
#
#     @api_view()
#     def student_list(request):
#         movies = StudentModel.objects.all()
#         serializer = StudentModelSerializer(movies, many=True)
#         print(serializer)
#         return Response(serializer.data)
#
# class ModuleList(generics.ListCreateAPIView):
#     queryset = ModuleModel.objects
#     serializer_class = ModuleModelSerializer
#
# class GradeList(generics.ListCreateAPIView):
#     queryset = GradesModel.objects
#     serializer_class = GradesModelSerializer
#
# class ClassList(generics.ListCreateAPIView):
#     queryset = ClassModel.objects.all()
#     serializer_class = ClassModelSerializer
#
# class AttendanceList(generics.ListCreateAPIView):
#     queryset = AttendanceLogModel.objects
#     serializer_class = AttendanceLogSerializer
#
#
# class AttendanceDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = AttendanceLogModel.objects
#     serializer_class = AttendanceLogSerializer

