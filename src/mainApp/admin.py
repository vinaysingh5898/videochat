from django.contrib import admin
# Register your models here.
from .models import * 
from .forms import *

# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
	list_display=["id","user","PriPhone","LandMark","City","State","Country","PinCode","AddressLine","Updated_at","Created_at"]
	form=UserInfoForm
	class Meta:
		model = UserInfo

class BookAdmin(admin.ModelAdmin):
	list_display= ["id","Title","Authors","Updated_at","Created_at"]
	# form=AddAuthorForm
	class Meta:
		model = Book

admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Cart)