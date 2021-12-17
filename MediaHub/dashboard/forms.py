from django.forms import ModelForm
from api.models import *

class addMovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['mediaTitle','mediaRelease','categories','medium','director']
    
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