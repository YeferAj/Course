from . import views
from django.urls import path, include
from rest_framework import routers
from .api import StudentViewSet

router = routers.DefaultRouter()
router.register('', StudentViewSet, 'students', )
urlpatterns = [
    path('', views.students, name='students'),
    path('', views.index, name='index'),
    path('delete_student/<int:id>', views.delete_student, name='delete_student'),
    path('edit_student/<int:id>', views.edit_student, name='edit_student'),
    path('view_student/<int:id>', views.view_student, name='view_student'),
    path('api/', include(router.urls)),
]