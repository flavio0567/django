from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'^$', views.new),
	url(r'^courses/create$', views.create),
	url(r'^courses/(?P<id>\d+)/confirmation$', views.confirmation),
	url(r'^courses/(?P<id>\d+)/destroy$', views.destroy),
    url(r'^courses/(?P<id>\d+)/comments$', views.comments),
	url(r'^courses/(?P<id>\d+)/newcomment$', views.newcomment),
]
