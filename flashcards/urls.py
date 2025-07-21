from django.urls import path
from . import views

urlpatterns = [
    path('fm_formulas/', views.fm_formulas, name='fm_formulas'),
]
