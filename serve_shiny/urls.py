from django.urls import path, include

from .views import hash_view, update_connection

urlpatterns = [
	path('hash/<int:id>/' , hash_view, name ='hash'),
	path('connect/' , update_connection, name = 'connection'), 
	]

