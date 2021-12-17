from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from api.models import *
import frontend.views
from .forms import *

# Create your views here.
def dashboard(request):
    return redirect(frontend.views.dashboard)

def manageMovies(request):
    return render(request, 'dashboard/dashboardManageMovies.html') 

def manageBooks(request):
    return render(request, 'dashboard/dashboardManageBooks.html')

def manageShows(request):
    return render(request, 'dashboard/dashboardManageShows.html') 

def manageVideoGames(request):
    return render(request, 'dashboard/dashboardManageVideoGames.html')

def managePlaylists(request):
    return render(request, 'dashboard/dashboardManagePlaylists.html') 

def sucessAdd(request):
    return render(request, 'dashboard/sucess.html')

def addMovie(request):
    form = addMovieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(sucessAdd)
    return render(request, 'dashboard/addMovie.html', {'form': form})

def addBook(request):
    form = addBookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(sucessAdd)
    return render(request, 'dashboard/addBook.html', {'form': form})

def addShow(request):
    form = addShowForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(sucessAdd)
    return render(request, 'dashboard/addShow.html', {'form': form})

def addVideoGame(request):
    form = addVideoGameForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(sucessAdd)
    return render(request, 'dashboard/addVideoGame.html', {'form': form})

def addCategoryGenre(request):
    form = addCategoryGenreForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(sucessAdd)
    return render(request, 'dashboard/addCategoryGenre.html', {'form': form})

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

def editPlaylist(request):
    instance = get_object_or_404(Playlist, playListUser=request.POST["playListUser"], playListName=request.POST["playListName"])
    form = editPlaylistForm(request.POST or None, instance=instance)
    form.fields["playListUser"].initial = request.POST["playListUser"]
    form.fields["playListName"].initial = request.POST["playListName"]
    return render(request, 'dashboard/editPlaylist.html', {'form':form})

def updatePlaylist(request):
    instance = get_object_or_404(Playlist, playListUser=request.POST["playListUser"], playListName=request.POST["playListName"])
    form = editPlaylistForm(request.POST or None, instance=instance)
    form.fields["playListUser"].initial = request.POST["playListUser"]
    form.fields["playListName"].initial = request.POST["playListName"]
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/dashboard/viewPlaylists')
    return render(request, 'dashboard/editPlaylist.html', {'form':form})
