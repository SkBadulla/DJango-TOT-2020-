from django.urls import path
from myApp2 import views
urlpatterns=[
	path('',views.hello,name='hello'),
	path('register/',views.register,name='register'),
]