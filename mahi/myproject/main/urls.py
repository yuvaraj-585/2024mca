from django.urls import path,include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('yuvaraj/', views.yuvaraj, name='yuvaraj'),
    path('prasad/', views.prasad, name='prasad'),
]

