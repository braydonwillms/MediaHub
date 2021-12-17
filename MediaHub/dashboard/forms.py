from django.forms import ModelForm
from api.models import *

class addMovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['mediaTitle','mediaRelease','categories','medium','director']