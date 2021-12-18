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

def manageFriends(request):
    return render(request, 'dashboard/dashboardManageFriends.html')

def managePlatforms(request):
    return render(request, 'dashboard/dashboardManagePlatforms.html')

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

class viewFriends(generic.ListView):
    model = User

    def get_queryset(self):
        username = self.request.session["username"]
        return User.objects.filter(userID=username)

def addFriend(request):
    if request.method == 'GET':
        return render(request, 'dashboard/addFriend.html', {"form":addFriendForm()})
    if request.method == 'POST':
        form = addFriendForm(request.POST)
        if form.is_valid():
            user = User.objects.get(userID=request.session["username"])
            try:
                user.friends.add(User.objects.get(userID=form.cleaned_data["friend_username"]))
                user.save()
                user2 = User.objects.get(userID=form.cleaned_data["friend_username"])
                user2.friends.add(User.objects.get(userID=request.session["username"]))
                user2.save()
                return HttpResponseRedirect('/dashboard/manageFriends')
            except:
                return redirect(addFriend)
    return redirect(addFriend)

def deleteMedia(request, mediaID):
    media = Media.objects.get(pk=mediaID)
    media.delete()
    return redirect('viewMedia')

def addPhysical(request):
    form = addPhysicalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(sucessAdd)
    return render(request, 'dashboard/addPhysical.html', {'form': form})

def addDevice(request):
    form = addDeviceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(sucessAdd)
    return render(request, 'dashboard/addDevice.html', {'form': form})

def addWebsite(request):
    form = addWebsiteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(sucessAdd)
    return render(request, 'dashboard/addWebsite.html', {'form': form})

class viewPlatforms(generic.ListView):
    model = Platform

def deletePlatform(request, platformID):
    platform = Platform.objects.get(pk=platformID)
    platform.delete()
    return redirect('viewPlatforms')

def suggestMedia(request):
    if request.method == 'POST':
        form = suggestMediaForm(request.session["username"], request.POST)
        if form.is_valid():
            suggestion = Suggestions(suggestorsUserID=User.objects.get(userID=form.cleaned_data["username"]),
                        suggesteeUserID=User.objects.get(userID=form.cleaned_data["friend_username"]),
                        suggestedMediaID=form.cleaned_data["media_suggestion"])
            suggestion.save()
            return redirect(manageFriends)
    form = suggestMediaForm(request.session["username"])
    form.fields["username"].initial = request.session["username"]
    return render(request, 'dashboard/suggestMedia.html', {'form': form})

class viewSuggestions(generic.ListView):
    model = Suggestions

    def get_queryset(self):
        username = self.request.session["username"]
        return Suggestions.objects.filter(suggesteeUserID=username)

def sharePlaylist(request):
    if request.method == 'POST':
        form = sharePlaylistForm(request.session["username"], request.POST)
        if form.is_valid():
            share = Shares(creatorUserID=User.objects.get(userID=form.cleaned_data["username"]),
                           sharedUserID=User.objects.get(userID=form.cleaned_data["friend_username"]),
                           sharedPlaylistID=form.cleaned_data["playlist_to_share"])
            share.save()
            return redirect(managePlaylists)
    form = sharePlaylistForm(request.session["username"])
    form.fields["username"].initial = request.session["username"]
    return render(request, 'dashboard/sharePlaylist.html', {'form': form})

class viewSharedPlaylists(generic.ListView):
    model = Shares

    def get_queryset(self):
        username = self.request.session["username"]
        return Shares.objects.filter(sharedUserID=username)
