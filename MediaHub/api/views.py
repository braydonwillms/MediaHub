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

	def put(self, request, format=None):
		serializer = ReviewSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddCategory(APIView):
	def post(self, request, format=None):
		serializer = CategorySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
