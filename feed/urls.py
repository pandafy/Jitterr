from django.urls import path
from . import views

urlpatterns = [
	#path('feed/<user_id>',views.feed,name = 'feed'),
   	path('',views.feed,name = 'feed'),
	path('notifications',views.notifications,name = 'notifications'),
	path('user/setings',views.settings, name = 'settings'),

	path('user/<int:user_id>',views.profile, name = 'profile')

	#path('',views.signin,name = 'signin')

	]