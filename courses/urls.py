from . import views
from django.urls import path, include
from rest_framework import routers
from .api import CourseViewSet

router = routers.DefaultRouter()
router.register('', CourseViewSet, 'courses', )

urlpatterns = [
    path('', views.courses, name='courses'),
    path('', views.index1, name='index1'),
    path('delete_course/<int:id>', views.delete_course, name='delete_course'),
    path('edit_course/<int:id>', views.edit_course, name='edit_course'),
    path('course_detail/<int:id>', views.course_detail, name='course_detail'),
    path('enrollments/add/', views.add_enrollment, name='add_enrollment'),
    path('enrollments/', views.enrollment_list, name='enrollment_list'),
    path('api/', include(router.urls)),
]