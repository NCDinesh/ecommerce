from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path("about",views.about, name="about"),
    path("blog",views.blog, name="blog"),
    path("cart",views.cart, name="cart"),
    path("contact",views.contact,name="contact"),
    path("sproduct",views.sproduct, name="sproduct"),
    path("shop",views.shop, name="shop")
]

