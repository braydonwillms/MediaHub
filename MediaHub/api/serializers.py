from . import models
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		fields = '__all__'

class UserUsernameSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		fields = ['userID']

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
		model = models.VideoGame
		fields = '__all__'

class VideoGameConsoleSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.VideoGameConsole
		fields = '__all__'

class ShowSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Show
		fields = '__all__'

class ShowSeasonsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.ShowSeasons
		fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.CatgegoryGenre
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

class PermissionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Permissions
		fields = '__all__'

class FriendsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Friends
		fields = '__all__'

class SuggestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Suggests
		fields = '__all__'

class SharesSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Shares
		fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Rating
		fields = '__all__'

class OwnsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Owns
		fields = '__all__'
