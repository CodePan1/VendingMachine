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
from machine.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('machine/create', vending_machine_create, name="create machine"),
    path('machine/edit', vending_machine_edit, name="edit machine"),
    path('machine/delete', vending_machine_delete, name="delete machine"),
    path('product/create', product_create, name="create product"),
    path('product/delete', product_delete, name="product delete"),
    path('product/stock', product_stock, name="product stock")

]
