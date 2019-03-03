from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import url
from .views import search

app_name = 'blog'

urlpatterns = [
    path('<int:blog_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('', views.blog, name='blog'),
    path('newblog/', views.blogpost, name="newblog"),
    url(r'^results/$', search, name='search'),
    path('me/', views.me, name="me"),
    url(r'^category/$', views.get_queryset, name='category'),
]