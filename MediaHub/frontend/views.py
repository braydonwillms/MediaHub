from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'frontend/index.html', context = context)

def login(request):
    context = {}
    return render(request, 'frontend/login.html', context=context)
