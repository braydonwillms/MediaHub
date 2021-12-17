from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from api.models import *
from .forms import *

# Create your views here.
def dashboard(request):
    context = {}
    return render(request, 'dashboard/dashboard.html', context)

def sucessAdd(request):
    context = {}
    return render(request, 'dashboard/sucess.html', context)

def addMovie(request):
    if request.method == "POST":
        form = addMovieForm(request.POST)
        if form.is_valid():
            form.save()
    else:
      form = addMovieForm()
    return render(request, 'dashboard/addMovie.html', {'form': form})
    
def addMovie(request):
    form = addMovieForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        #do stuff here if you need to
        obj.save()
        form = addMovieForm()
        return HttpResponseRedirect('/dashboard/sucess')
    return render(request, 'dashboard/addMovie.html', {'form': form})

class viewMedia(generic.ListView):
    model = Media


# def viewMedia(request):
#     context = {}
#     return render(request, 'dashboard/viewMedia.html', context)