"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from machine import views
from machine.views import *

urlpatterns = [
    path('vending-machine/create/', views.vending_machine_create, name='vending_machine_create'),
    path('vending-machine/<int:pk>/edit/', views.vending_machine_edit, name='vending_machine_edit'),
    path('vending-machine/<int:pk>/delete/', views.vending_machine_delete, name='vending_machine_delete'),
    path('vending-machine/<int:vending_machine_pk>/product/create/', views.product_create, name='product_create'),
    path('vending-machine/<int:vending_machine_pk>/product/<int:product_pk>/edit/', views.product_edit,
         name='product_edit'),
    path('vending-machine/<int:vending_machine_pk>/product/<int:product_pk>/delete/', views.product_delete,
         name='product_delete'),
    path('vending-machine/<int:vending_machine_pk>/product/<int:product_pk>/stock/', views.product_stock,
         name='product_stock'),
]