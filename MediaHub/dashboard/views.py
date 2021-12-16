from django.shortcuts import render
from django.views import generic
from api.models import *

# Create your views here.
def dashboard(request):
    context = {}
    return render(request, 'dashboard/dashboard.html', context)

def addMedia(request):
    context = {}
    return render(request, 'dashboard/addMedia.html', context)

class viewMedia(generic.ListView):
    model = Movie


# def viewMedia(request):
#     context = {}
#     return render(request, 'dashboard/viewMedia.html', context)