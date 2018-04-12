from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
	user=models.ForeignKey(User)
	PriPhone=models.DecimalField(max_digits=10, decimal_places=False,blank=False)
	LandMark=models.CharField(max_length=500,blank=True,null=True)
	City=models.CharField(max_length=500, default='')
	State=models.CharField(max_length=500, default='')
	Country=models.CharField(max_length=500,default='')
	PinCode=models.DecimalField(max_digits=6, decimal_places=False,blank=False)
	AddressLine=models.CharField(max_length=500,blank=True,null=True)
	Updated_at=models.DateTimeField(auto_now_add=False,auto_now=True)
	Created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
	def __str__(self):
		return self.user.username

class Book(models.Model):
	Title=models.CharField(max_length=120,blank=False,null=True)
	Authors=models.CharField(max_length=120,blank=False,null=True)
	Updated_at=models.DateTimeField(auto_now_add=False,auto_now=True)
	Created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
	def __str__ (self): #	python 3.3 is __str__
		return self.Title

class Cart(models.Model):
	BookId=models.ForeignKey(Book)
	UserId=models.ForeignKey(User)
	def __str__(self):
		return str(self.UserId)