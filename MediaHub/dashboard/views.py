from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from api.models import *
import frontend.views
from .forms import *

# Create your views here.
def dashboard(request):
    return redirect(request ,frontend.views.dashboard)

def manageMovies(request):
    return render(request, 'dashboard/dashboardManageMovies.html') 

def manageBooks(request):
    return render(request, 'dashboard/dashboardManageBooks.html')

def manageShows(request):
    return render(request, 'dashboard/dashboardManageShows.html') 

def manageVideoGames(request):
    return render(request, 'dashboard/dashboardManageVideoGames.html') 

def sucessAdd(request):
    return render(request, 'dashboard/sucess.html')
    
def addMovie(request):
    form = addMovieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('sucess/')
    return render(request, 'dashboard/addMovie.html', {'form': form})

def addBook(request):
    form = addBookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('sucess/')
    return render(request, 'dashboard/addBook.html', {'form': form})

def addShow(request):
    form = addShowForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('sucess/')
    return render(request, 'dashboard/addShow.html', {'form': form})

def addVideoGame(request):
    form = addVideoGameForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('sucess/')
    return render(request, 'dashboard/addVideoGame.html', {'form': form})

class viewMedia(generic.ListView):
    model = Media

