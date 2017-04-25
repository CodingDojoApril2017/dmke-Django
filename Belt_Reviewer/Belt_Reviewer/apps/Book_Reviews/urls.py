from django.conf.urls import url
from . import views           # So we can call functions from our routes!
urlpatterns = [
	## books/ root route
	url(r'^$', views.render_home, name = 'render_home'),       # 'home' route.
	## books/add/ route
	url(r'^render_add/', views.render_add, name = 'render_add'),
	url(r'^process_add/', views.process_add, name = 'process_add'),
	url(r'^test/', views.render_book, name = 'render_book'),
	url(r'^(?P<book_id>[0-9]+)$', views.render_book, name = 'render_book')
]
