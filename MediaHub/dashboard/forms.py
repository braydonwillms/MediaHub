from django.forms import ModelForm, HiddenInput, CheckboxSelectMultiple
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


