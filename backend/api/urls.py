from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('/Student', views.StudentList.as_view()),
]