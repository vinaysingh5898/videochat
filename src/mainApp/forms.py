from django import forms
from .models import *
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

class LoginForm(forms.Form):
	username=forms.CharField()
	password= forms.CharField(widget=forms.PasswordInput)
		
	def clean(self,*args,**kwargs):
		username=self.cleaned_data.get("username")
		password=self.cleaned_data.get("password")
		user=authenticate(username=username,password=password)
		if not user:
			raise forms.ValidationError("This User does not exits")
		if not user.check_password(password):
			raise forms.ValidationError("Incorrect Password")
		if not user.is_active:
			raise forms.ValidationError("This User is no longer active")
		return super(LoginForm,self).clean(*args,**kwargs)

class RegistrationForm(forms.ModelForm):
	password= forms.CharField(widget=forms.PasswordInput,label="Password")
	password2= forms.CharField(widget=forms.PasswordInput,label="Confirm Password")
	email=forms.EmailField(label="Email Address")

	class Meta:
		model=User
		fields=[
		"username",
		"email",
		"first_name",
		"last_name",
		"password",
		]
	def clean_password2(self):
		password=self.cleaned_data.get("password")
		password2=self.cleaned_data.get("password2")
		if password != password2:
			raise forms.ValidationError("Two Password Must Match.")
		return password
	def clean_email(self):
		email=self.cleaned_data.get("email")
		email_qs=User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("This email has already been registered.")
		return email

class UserInfoForm(forms.ModelForm):
	class Meta:
		model=UserInfo
		fields=[
		'PriPhone',
		'LandMark',
		'City',
		'State',
		'Country',
		'PinCode',
		'AddressLine',
		]

class BookForm(forms.ModelForm):
	class Meta:
		model=Book
		fields=[
		'Title',
		'Authors',
		]
	def clean_Title(self):
		Title=self.cleaned_data.get("Title")
		title_qs=Book.objects.filter(Title=Title)
		if title_qs.exists():
			raise forms.ValidationError("This title is already exists.")
		return Title