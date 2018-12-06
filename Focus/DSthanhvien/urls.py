from django.urls import path
from DSthanhvien import views
urlpatterns = [
    path('', views.list),
]