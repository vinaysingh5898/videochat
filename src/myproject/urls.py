from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registration/$','mainApp.views.registration',name='registration'),
    url(r'^login/$','mainApp.views.login_function',name='login'),
    url(r'^show_data/$','mainApp.views.show_data',name='show_data'),
    url(r'^add-to-cart/(?P<Book_id>\d+)','mainApp.views.addToCart',name='add-to-cart'),
    url(r'^chatroom/(?P<Uname>\w+)','mainApp.views.chatroom',name='chatroom'),
    url(r'^delete-book-from-cart/(?P<id>\d+)','mainApp.views.deleteBookFromCart',name='delete-book-from-cart'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page':'/login'},name='logout')
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


	 # url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page':'/login'},name='logout')