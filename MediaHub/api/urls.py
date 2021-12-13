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
	path('category/', views.AddCategory.as_view()),
]
