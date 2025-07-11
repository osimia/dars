from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lesson/<int:id>/', views.lesson_detail, name='lesson_detail'),
    path('run_code/', views.run_code, name='run_code'),
]
