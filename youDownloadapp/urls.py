from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('',views.index,name='index'),
    path('video',views.download,name='video'),
]