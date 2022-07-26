from calendar import c
from django.contrib import admin
from django.urls import path, include

from api import views


urlpatterns = [path('orders/', views.query_by_brand_id),
                path('orders/products/', views.query_products_by_id_or_reference),   
             ]
    