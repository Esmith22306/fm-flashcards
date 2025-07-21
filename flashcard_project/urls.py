from django.contrib import admin
from django.urls import include, path
from flashcards import views


urlpatterns = [
    path('flashcards/', include('flashcards.urls')),
    path('', views.home, name='home'),  # assuming you have a home view
]
