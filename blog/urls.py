from django.conf.urls import patterns,url,include
from blog import views

urlpatterns = patterns('',
	url(r'^$',views.home,name='home'),
)