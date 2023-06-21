from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('product',views.product_page,name='products'),
    path('product/<key>',views.filter_prod,name='filter_product'),
    path('<uuid:pid>/product',views.single_prod,name='product_view'),
    path('<uuid:pid>/quotation',views.request_quote,name='rfq'),
]