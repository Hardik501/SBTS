from django.urls import path, include
from . import views

from django.views.decorators.cache import cache_page

urlpatterns = [
    path('register/', views.StudentRegistrationView.as_view(), name='student_registration'),
    path('enroll-course/', views.StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    path('course/<int:pk>/', cache_page(60 * 15)(views.StudentCourseDetailView.as_view()), name='student_course_detail'),
    path('course/<int:pk>/<int:module_id>/', cache_page(60 * 15)(views.StudentCourseDetailView.as_view()), name='student_course_detail_module'),
    path('courses/', views.StudentCourseListView.as_view(), name='student_course_list'),

]