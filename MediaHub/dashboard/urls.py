from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('addMovie/', views.addMovie, name='addMovie'),
    path('viewMedia/', views.viewMedia.as_view(), name='viewMedia')
]