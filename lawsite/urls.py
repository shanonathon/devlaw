from django.conf.urls import patterns, url, include
from lawsite import views	


urlpatterns = patterns('',

	url(r'^$', views.home, name='home'),

)