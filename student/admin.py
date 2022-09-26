from django.contrib import admin
from .models import Student,College,Teacher
# Register your models here.

class CollegeAdmin(admin.ModelAdmin):
    list_display = ("id", 'college_name','college_address','slug')
    search_fields = ("id", "college_name")
    readonly_fields = ("id", )
    ordering = ['college_name']
    list_display_links = ('college_name', )

class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", 'teacher_name','teacher_subject','slug')
    search_fields = ("id", "teacher_name")
    readonly_fields = ("id", )
    ordering = ['teacher_name']
    list_display_links = ('teacher_name', )

class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", 'student_name','student_roll_no','college','guide','slug')
    search_fields = ("id", "student_name")
    readonly_fields = ("id", )
    ordering = ['student_roll_no']
    list_display_links = ('student_name', )

admin.site.register(Student, StudentAdmin)
admin.site.register(College, CollegeAdmin)
admin.site.register(Teacher , TeacherAdmin)