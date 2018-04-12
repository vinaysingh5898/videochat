from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponseRedirect

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)


# Create your views here.

def login_function(request):
	title="You are loged in"
	form=LoginForm(request.POST or None)
	print("1")
	if form.is_valid():
		username=form.cleaned_data.get("username")
		password=form.cleaned_data.get("password")
		user=authenticate(username=username,password=password)
		login(request,user)
		print("2")
	if request.user.is_authenticated():
		print("3")
		form2=BookForm(request.POST or None)
		if form2.is_valid():
			profile=form2.save(commit=False)
			profile.User_id=request.user.id
			profile.save()
			return HttpResponseRedirect('../login')	
		return render(request,"check.html",{"form":form,"form2":form2,"title":title})
	return render(request,"login.html",{"form":form})

def registration(request):
	form1=RegistrationForm(request.POST or None)
	form2=UserInfoForm(request.POST or None)
	context={"form1":form1,"form2":form2}
	if form1.is_valid():
		title='You are registered successfully!'
		user=form1.save(commit=False)
		password=form1.cleaned_data.get('password')
		username=form1.cleaned_data.get('username')
		user.set_password(password)
		user.save()
		new_user=authenticate(username=user.username,password=password)
		login(request,new_user)
		userprofile=form2.save(commit=False)
		# userprofile.User=username
		userprofile.user_id=request.user.id
		t=userprofile.save()

	if(request.user.is_authenticated()):
		return render(request,"check.html",context)
	return render(request,"registration.html",context)

def deleteBookFromCart(request,id=None):
	book=''
	if(request.user.is_authenticated()):
		bookd=Book.objects.get(id=id)
		bookd.delete()
		book=Book.objects.filter()
	return render(request,"show.html" ,{"book":book})

def addToCart(request,Book_id=None):
	#print(request.user.id)
	#cartObj=Cart.objects.filter(Book_id=Book_id,user_id=request.user.id)
	#Quantity=1;
	book=''
	if(request.user.is_authenticated()):
		book=Book.objects.filter()
		cartObject=Cart()
		cartObject.UserId_id=request.user.id
		print(cartObject.UserId)
		# cartObject.Quantity=1;
		cartObject.BookId_id=Book_id
		cartObject.save()
		#check=0
	return render(request,"show.html" ,{"book":book})



def show_data(request):
	if(request.user.is_authenticated()):
		book=Book.objects.filter()
		return render(request,"show.html",{"book":book})
	return render(request,"registration.html",context)