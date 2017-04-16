from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^aboutme$', views.aboutme),
    url(r'^projects$', views.projects),    
    url(r'^testimonials$', views.testimonials)
]