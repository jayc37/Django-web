from django.test import TestCase

# Create your tests here.
from django.urls import path
from DSthanhvien import views
urlpatterns = [
    path('', views.list),
]