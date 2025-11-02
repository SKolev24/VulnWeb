from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='products_list'),
    path('<str:product_name>/', views.product_detail, name='products_detail'),

]