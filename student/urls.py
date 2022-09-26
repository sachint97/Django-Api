from django.urls import path
from .views import StudentView
urlpatterns = [
    path('students/', StudentView.as_view(), name='students_get'),
    path('student/create/',StudentView.as_view(), name='students_post'),
    path('student/update/<str:slug>/',StudentView.as_view(), name='students_put'),
    path('student/delete/<str:slug>/',StudentView.as_view(), name='students_delete')
]