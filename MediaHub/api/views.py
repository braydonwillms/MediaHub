from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from .serializers import *

class AddAdmin(APIView):
	def post(self, request, format=None):
		serializer = AdminSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminDetails(APIView):
	def get(self, request, adminID, format=None):
		try:
			admin = models.Admin.objects.get(adminID=adminID)
			serializer = AdminNameSerializer(admin)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)

class VerifyAdmin(APIView):
	def get(self, request, adminID, adminPassword, format=None):
		try:
			admin = models.Admin.objects.get(adminID=adminID, adminPassword=adminPassword)
			return Response('{ "valid":true }', status=status.HTTP_200_OK)
		except:
			return Response('{ "valid":false }', status=status.HTTP_200_OK)

class AddUser(APIView):
	def post(self, request, format=None):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyUser(APIView):
	def get(self, request, userID, userPassword, format=None):
		try:
			user = models.User.objects.get(userID=userID, userPassword=userPassword)
			return Response('{ "valid":true }', status=status.HTTP_200_OK)
		except:
			return Response('{ "valid":false }', status=status.HTTP_200_OK)

class UserDetails(APIView):
	def get(self, request, userID, format=None):
		try:
			user = models.User.objects.get(userID=userID)
			serializer = UserNameSerializer(user)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)

class AddReview(APIView):
	def post(self, request, format=None):
		serializer = ReviewSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, sattus=status.HTTP_400_BAD_REQUEST)

class EditReview(APIView):
	def put(self, request, reviewID, format=None):
		review = models.Review.objects.filter(reviewID=reviewID).first()
		serializer = ReviewSerializer(review, request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class AddCategory(APIView):
	def post(self, request, format=None):
		serializer = CategorySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddBook(APIView):
	def post(self, request, format=None):
		serializer = BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddMovie(APIView):
	def post(self, request, format=None):
		serializer = MovieSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddVideoGame(APIView):
	def post(self, request, format=None):
		serializer = VideoGameSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddShow(APIView):
	def post(self, request, format=None):
		serializer = ShowSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetMedia(APIView):
	def get(self, request, format=None):
		media = models.Media.objects.all()
		serializer = MediaSerializer(media, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class MediaDetails(APIView):
	def get(self, request, mediaID, format=None):
		try:
			media = models.Book.objects.get(mediaID=mediaID)
			serializer = BookSerializer(media)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except:
			try:
				media = models.Movie.objects.get(mediaID=mediaID)
				serializer = MovieSerializer(media)
				return Response(serializer.data, status=status.HTTP_200_OK)
			except:
				try:
					media = models.Show.objects.get(mediaID=mediaID)
					serializer = ShowSerializer(media)
					return Response(serializer.data, status=status.HTTP_200_OK)
				except:
					try:
						media = models.VideoGame.objects.get(mediaID=mediaID)
						serializer = VideoGameSerializer(media)
						return Response(serializer.data, status=status.HTTP_200_OK)
					except:
						return Response(status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, mediaID, format=None):
		media = models.Media.objects.filter(mediaID=mediaID)
		media.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
