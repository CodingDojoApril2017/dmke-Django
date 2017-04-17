from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register', views.register),
    url(r'^wall', views.wall),
    url(r'^login', views.login),
    url(r'^messageR', views.messageR),
]