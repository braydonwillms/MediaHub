from django.db import models as fields
from . import models
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		fields = '__all__'

class UserNameSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		fields = ['userName']

class UserCredentialSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		fields = ['userID', 'userPassword']

class AdminSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Admin
		fields = '__all__'

class AdminUsernameSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Admin
		fields = ['adminID']

class AdminNameSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Admin
		fields = ['adminFirstName', 'adminLastName']

class AdminCredentialSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Admin
		fields = ['adminID','adminPassword']

class MediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Media
		fields = '__all__'

class MediaIdSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Media
		fields = ['mediaID']

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Book
		fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Movie
		fields = '__all__'

class VideoGameSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.VideoGameConsole
		fields = ['videoGameConsoleMediaID']

class VideoGameConsoleSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.VideoGameConsole
		fields = '__all__'

class ShowSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.ShowSeasons
		fields = ['showSeasonMediaID']

class ShowSeasonsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.ShowSeasons
		fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.CategoryGenre
		fields = '__all__'

class PlatformSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Platform
		fields = '__all__'

class PlatformIDSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Platform
		fields = ['platformID']

class PhysicalSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Physical
		fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Device
		fields = '__all__'

class WebsiteSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Website
		fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Review
		fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Playlist
		fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Permission
		fields = '__all__'

class FriendsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		fields = ['userID', 'friends']

class SuggestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Suggestions
		fields = '__all__'

class SharesSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Shares
		fields = '__all__'

class RatesSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Rates
		fields = '__all__'
