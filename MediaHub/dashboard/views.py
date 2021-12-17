from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from api.models import *
import frontend.views
from .forms import *

# Create your views here.
def dashboard(request):
    return redirect(frontend.views.dashboard)

def sucessAdd(request):
    context = {}
    return render(request, 'dashboard/sucess.html', context)

def addMovie(request):
    form = addMovieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/dashboard/sucess')
    return render(request, 'dashboard/addMovie.html', {'form': form})

class viewMedia(generic.ListView):
    model = Media

class viewPlaylists(generic.ListView):
    model = Playlist

    def get_queryset(self):
        username = self.request.session["username"]
        return Playlist.objects.filter(playListUser=username)

def addPlaylist(request):
    form = addPlaylistForm(request.POST or None)
    form.fields["playListUser"].initial = request.session["username"]
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/dashboard/viewPlaylists')
    return render(request, 'dashboard/addPlaylist.html', {'form':form})
