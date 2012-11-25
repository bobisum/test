from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect
from users.forms import RegisterForm, LoginForm

def register_user(request):

	if request.method == "POST":
		form = RegisterForm(request.POST)

		if form.is_valid():
			form.save()

			data = form.cleaned_data
			user = authenticate(username=data['username'], password=data['password'])

			return HttpResponseRedirect('/registerSucces/')

	else:
		form = RegisterForm()

	return render(request, 'register.html', {'form':form})


def login_user(request):

	if request.method == "POST":
		form = LoginForm(request.POST)

		if form.is_valid():
			data = form.cleaned_data
			user = authenticate(username=data['username'], password=data['password'])

			if user is not None:
				if user.is_active:
					login(request, user)

					return HttpResponseRedirect('/loginSucces/')
				else:
					return HttpResponseRedirect('/loginError/')
			else:
				return HttpResponseRedirect('/loginError/')

	else:
		form = LoginForm()

	return render(request, 'login.html', {'form':form})

def logout_user(request):
	
	logout(request)

	return HttpResponseRedirect('/home/')