from django.contrib import admin
from django.urls import path
from . import views, models
from .views import PostDetailView

urlpatterns = [
    path('', views.home,name='blog-home'),
    path('animes/', views.animelist,name='blog-list'),
    path('about_us/', views.about,name='blog-about'),
    path('contact/', views.contact,name='blog-contact'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

]
