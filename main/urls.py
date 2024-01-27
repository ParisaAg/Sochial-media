from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('signup', views.signup, name='signup'),
path('like', views.like, name='like'),
path('signin', views.signin, name='signin'),
path('logout', views.logout, name='logout'),
path('post', views.post, name='post'),
path('accounts', views.accounts, name='accounts'),
path('profile/<str:pk>/', views.profile, name='profile'),
]
