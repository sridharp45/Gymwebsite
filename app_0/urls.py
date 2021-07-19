from django.contrib import admin
from django.urls import path
from app_0 import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contacts',views.contacts,name='contacts'),
    path('dietplan',views.dietplan,name='diet'),
    path('workoutplan',views.workoutplan,name='workout'),
    path('contact',views.contact,name="contact")
]