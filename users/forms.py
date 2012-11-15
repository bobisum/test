from django import forms
from django.forms.widgets import PasswordInput
from django.contrib.auth.models import User

class RegisterForm(forms.Form):

	username = forms.CharField(min_lenght=3, required=True)
	email = forms.EmailFiled(required=True)
	password = forms.CharField(widget=forms.PasswordInput, min_lenght=3)

	def clean_username(self):
		username = self.cleaned_data['username']
		check_username = User.object.filter(username = username)

		if check_user_name:
			raise forms.ValidationError('This username is taken.')

		return username

	def clean_email(self):
		email = self.cleaned_data['email']
		check_email = User.object.filter(email = email)

		if check_email:
			raise forms.ValidationError('This is an invalid email.')

		return email

	def save(self):
		data = self.cleaned_data
		new_user = User.objects.create_user(data['username'], data['email'], data['password'])

		return new_user

class LoginForm(forms.Form):

	username = forms.CharField()
	

	password = forms.CharField(widget=forms.PasswordInput)

	def clean():

		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		
		if username and password:

			user = authenticate(username = username, password = password)


		return self.cleaned_data