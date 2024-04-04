from django.contrib import admin
from django.urls import path
import app.views as views


urlpatterns = [
    path('', views.index, name='index'),
    path('service', views.service, name='service'),
    path('gallery', views.gallery, name='gallery'),
    path('blog', views.blog, name='blog'),
    path('contactUs', views.contactus, name='contactus'),
    path('money', views.money, name='money'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('team', views.team, name='team'),
    path('news', views.news, name='news'),
    path('carieers', views.carieers, name='carieers'),
    path('newsDsc', views.newsDsc, name="newsDsc"),
    path('carierdes', views.carierdes, name="carierdes"),

]
