from django.urls import path

from . import views

urlpatterns = [
    path('musicon/', views.musicon),
]