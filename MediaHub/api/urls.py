from django.urls import path

from . import views
urlpatterns = [
	path('admin/', views.AddAdmin.as_view()),
	path('admin/<str:adminID>', views.AdminDetails.as_view()),
	path('admin/<str:adminID>/<str:adminPassword>', views.VerifyAdmin.as_view()),
	path('users/', views.AddUser.as_view()),
	path('users/<str:userID>', views.UserDetails.as_view()),
	path('users/<str:userID>/<str:userPassword>', views.VerifyUser.as_view()),
	path('reviews/', views.AddReview.as_view()),
	path('reviews/<int:reviewID>', views.EditReview.as_view()),
	path('category/', views.AddCategory.as_view()),
	path('media/book/', views.AddBook.as_view()),
	path('media/movie/', views.AddMovie.as_view()),
	path('media/show/', views.AddShow.as_view()),
	path('media/game/', views.AddVideoGame.as_view()),
	path('media/', views.GetMedia.as_view()),
	path('media/<int:mediaID>', views.MediaDetails.as_view()),
]
