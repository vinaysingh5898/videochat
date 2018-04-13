from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
	user=models.ForeignKey(User)
	PriPhone=models.DecimalField(max_digits=10, decimal_places=False)
	City=models.CharField(max_length=500, default='',blank=True)
	State=models.CharField(max_length=500, default='',blank=True)
	Country=models.CharField(max_length=500,default='',blank=True)
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