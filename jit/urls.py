from django.urls import path
from . import views

urlpatterns = [
	path('<int:jit_id>',views.jit,name = 'jit'),
    path('new_post',views.new_post,name = 'new_post'),
	path('new_post1',views.new_post1,name = 'new_post1'),
	path('liked',views.liked, name = "liked"),

	#path('',views.signin,name = 'signin')

	]