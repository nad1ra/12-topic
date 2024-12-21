from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('list/', views.student_list, name='list'),
    path('student/create/', views.student_create, name='add'),
    path('student/detail/', views.student_detail, name='add'),
]
