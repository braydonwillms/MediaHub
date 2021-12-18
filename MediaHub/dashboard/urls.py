from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('manageMovies/', views.manageMovies, name='manageMovies'),
    path('manageBooks/', views.manageBooks, name='manageBooks'),
    path('manageShows/', views.manageShows, name='manageShows'),
    path('manageVideoGame/', views.manageVideoGames, name='manageVideoGames'),
    path('managePlaylists/', views.managePlaylists, name='managePlaylists'),
    path('manageFriends/', views.manageFriends, name='manageFriends'),
    path('managePlatforms/', views.managePlatforms, name='managePlatforms'),
    path('addMovie/', views.addMovie, name='addMovie'),
    path('addBook/', views.addBook, name='addBook'),
    path('addShow/', views.addShow, name='addShow'),
    path('addVideoGame/', views.addVideoGame, name='addVideoGame'),
    path('addCategoryGenre', views.addCategoryGenre, name='addCategoryGenre'),
    path('addPhysical', views.addPhysical, name='addPhysical'),
    path('addDevice', views.addDevice, name='addDevice'),
    path('addWebsite', views.addWebsite, name='addWebsite'),
    path('viewMedia/', views.viewMedia.as_view(), name='viewMedia'),
    path('viewPlaylists/', views.viewPlaylists.as_view(), name='viewPlaylists'),
    path('addPlaylist/', views.addPlaylist, name='addPlaylist'),
    path('sucess/', views.sucessAdd, name='sucess'),
    path('editPlaylist/', views.editPlaylist, name='editPlaylist'),
    path('updatePlaylist/', views.updatePlaylist, name='updatePlaylist'),
    path('addMovie/sucess/', views.sucessAdd, name='sucess'),
    path('addFriend/', views.addFriend, name='addFriend'),
    path('viewFriends/', views.viewFriends.as_view(), name='viewFriends'),
    path('deleteMedia/ <mediaID> /', views.deleteMedia, name='deleteMedia'),
    path('deletePlatform/ <platformID> /', views.deletePlatform, name='deletePlatform'),
    path('viewPlatforms/', views.viewPlatforms.as_view(), name='viewPlatforms')
    path('suggestMedia/', views.suggestMedia, name='suggestMedia'),
    path('viewSuggestions/', views.viewSuggestions.as_view(), name='viewSuggestions')
]