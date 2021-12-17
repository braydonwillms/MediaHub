from django.shortcuts import render, redirect
from django.views import generic
from api.models import *
import frontend.views
from .forms import *

# Create your views here.
def dashboard(request):
    return redirect(frontend.views.dashboard)

def addMovie(request):
    if request.method == "POST":
        form = addMovieForm(request.POST)
        if form.is_valid():
            form.save()
    else:
      form = addMovieForm()
    return render(request, 'dashboard/addMovie.html', {'form': form})

class viewMedia(generic.ListView):
    model = Media


# def viewMedia(request):
#     context = {}
#     return render(request, 'dashboard/viewMedia.html', context)
