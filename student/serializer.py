from rest_framework import serializers

from .models import Student,Teacher,College

class CollegeSerializer(serializers.ModelSerializer):
    college_name = serializers.CharField(required=True, min_length=3, max_length=100)
    college_address = serializers.CharField(required=True, min_length=3, max_length=100)
    class Meta:
        model = College
        fields = ['college_name', 'college_address','slug']

class TeacherSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(required=True, min_length=3, max_length=100)
    teacher_subject = serializers.CharField(required=True, min_length=3, max_length=100)
    class Meta:
        model = Teacher
        fields = ['teacher_name', 'teacher_subject','slug']

class StudentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(required = True , min_length = 3 , max_length = 100)
    student_roll_no =serializers.IntegerField(required = True ,min_value=0, max_value=1000)
    college = CollegeSerializer(read_only=True)
    guide = TeacherSerializer(read_only = True)
    class Meta:
        model = Student
        fields = ['student_name', 'student_roll_no', 'college', 'guide','slug']

