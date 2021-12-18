from django.db.models.base import Model
from django.forms import ModelForm, HiddenInput, CheckboxSelectMultiple
from django import forms
from api.models import *

class addMovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['mediaTitle','mediaRelease','categories','medium','director']

class addPlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = '__all__'
        widgets = {
            'playListUser': HiddenInput(),
            'playListContains': CheckboxSelectMultiple
        }
        labels= {
            "playListName": "Name",
            "playListContains": "Playlist Items"
        }

class editPlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = '__all__'
        widgets = {
            'playListUser': HiddenInput(),
            'playListName': HiddenInput(),
            'playListContains': CheckboxSelectMultiple
        }
        labels = {
            "playListContains": "Playlist Items"
        }
    

class addBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['mediaTitle','mediaRelease', 'categories', 'author', 'ISBN']

class addShowForm(ModelForm):
    class Meta:
        model = Show
        fields = ['mediaTitle', 'mediaRelease']

class addVideoGameForm(ModelForm):
    class Meta:
        model = VideoGame
        fields = ['mediaTitle', 'mediaRelease']

class addCategoryGenreForm(ModelForm):
    class Meta:
        model = CategoryGenre
        fields = ['categoryGenreID', 'categoryGenreDescription']

class addFriendForm(forms.Form):
    friend_username = forms.CharField(max_length=50)

class suggestMediaForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.HiddenInput())

    def __init__(self, name, *args, **kwargs):
        super(suggestMediaForm, self).__init__(*args, **kwargs)

        self.fields["friend_username"] = forms.ModelChoiceField(queryset=User.objects.get(userID=name).friends.all())
        self.fields["media_suggestion"] = forms.ModelChoiceField(queryset=Media.objects.all())

class sharePlaylistForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.HiddenInput())

    def __init__(self, name, *args, **kwargs):
        super(sharePlaylistForm, self).__init__(*args, **kwargs)

        self.fields["friend_username"] = forms.ModelChoiceField(queryset=User.objects.get(userID=name).friends.all())
        self.fields["playlist_to_share"] = forms.ModelChoiceField(queryset=Playlist.objects.filter(playListUser=name))
