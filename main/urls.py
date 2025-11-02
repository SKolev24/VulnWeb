from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('search/', views.vulnerable_search, name='vulnerable_search'),
]