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
