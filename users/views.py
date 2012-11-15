from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from hello.users.forms import Register_form, Login_form


def register_user(request):

	if request.method == "POST":
		form = Register_form(request.POST)

		if form.is_valid():
			form.save()

			data = form.cleaned_data
			user = authenticate(username=data['user_name'], password=data['password'])


def login_user


def logout_user(request):
	
	logout(request)

	return