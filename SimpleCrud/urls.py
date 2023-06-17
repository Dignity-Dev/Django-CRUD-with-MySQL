
from django.contrib import admin
from django.urls import path
from StudentApp import views

urlpatterns = [
    path('', views.studentApi, name='student_home'),  # GET and POST requests
    path('student/', views.studentApi, name='student_list'),  # GET and POST requests
    path('student/<int:id>/', views.studentApi, name='student_detail'),  # PUT and DELETE requests
    path('admin/', admin.site.urls),
]