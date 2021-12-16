from django.shortcuts import render, redirect
import requests
import json

URL = "http://localhost:8000/"

def index(request):
	return render(request, 'index.html')

def login(request):
	return render(request, 'login.html')

def dashboard(request):
	try:
		if request.session["username"] != "":
			context = {"name":request.session["username"]}
			return render(request, 'dashboard.html', context)
		else:
			return redirect(login)
	except:
		return redirect(login)

def authenticate(request):
	username = request.GET["uname"]
	password = request.GET["psw"]
	r = requests.get(URL + "api/users/" + username + "/" + password)

	if r.status_code == 200:
		response = json.loads(r.json())
		if response["valid"]:
			request.session["username"] = username
			return redirect(dashboard)
	return redirect(login)

def logout(request):
	request.session["username"] = ""
	return redirect(index)
