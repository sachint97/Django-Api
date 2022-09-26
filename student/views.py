from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import Student,Teacher,College
from .serializer import CollegeSerializer,TeacherSerializer, StudentSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class StudentView(APIView):
    serializer_class = StudentSerializer

    def get(self,request):
        # student_qry = Student.objects.all()
        # serializer = self.serializer_class(student_qry,many=True)
        # return Response(serializer.data , status=status.HTTP_200_OK)
        paginator = PageNumberPagination()
        student_qry = Student.objects.all().order_by('student_roll_no')
        print(student_qry)
        context = paginator.paginate_queryset(student_qry,request)
        serializer = self.serializer_class(context, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self,request):        
        college_name=request.data['college']['college_name']
        college = College.objects.get(college_name=college_name)
        guide_name=request.data['guide']['teacher_name']
        guide = Teacher.objects.get(teacher_name = guide_name)
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(college=college,guide=guide)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def put(self,request, slug):
        try:
            queryset = Student.objects.get(slug = slug)
            serializer = self.serializer_class(queryset,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response("Student details updated", status = status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response("Student doesnot exist", status = status.HTTP_404_NOT_FOUND)

    def delete(self,request,slug):
        try:
            student = Student.objects.get(slug=slug)
            student.delete()
            return Response('Student delete successful', status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response("Student doesnot exist", status = status.HTTP_404_NOT_FOUND)

        