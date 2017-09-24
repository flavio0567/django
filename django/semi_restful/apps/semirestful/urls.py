from django.conf.urls import url
from . import views   

urlpatterns = [
    url(r'^$', views.users),
    url(r'^users/new$', views.new),
    url(r'^users/create$', views.create),
    url(r'^users/(\d+)$', views.show),
    url(r'^users/(\d+)/edit$', views.edit),
    url(r'^users/update/(\d+)$', views.update),
    url(r'^users/(\d+)/destroy$', views.destroy)
]