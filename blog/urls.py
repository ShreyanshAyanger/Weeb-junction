from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='blog-home'),
    path('animes/', views.animelist,name='blog-list'),
    path('about_us/', views.about,name='blog-about'),
    path('contact/', views.contact,name='blog-contact'),

]
