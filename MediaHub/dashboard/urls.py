from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('manageMovies/', views.manageMovies, name='manageMovies'),
    path('manageBooks/', views.manageBooks, name='manageBooks'),
    path('manageShows/', views.manageShows, name='manageShows'),
    path('addMovie/', views.addMovie, name='addMovie'),
    path('addBook/', views.addBook, name='addBook'),
    path('addShow/', views.addShow, name='addShow'),
    path('viewMedia/', views.viewMedia.as_view(), name='viewMedia'),
    path('sucess/', views.sucessAdd, name='sucess')
]