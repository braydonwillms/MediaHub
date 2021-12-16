from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('addMedia/', views.addMedia, name='addMedia'),
    path('viewMedia/', views.viewMedia.as_view(), name='viewMedia')
]