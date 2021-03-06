from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("", views.home, name="home"),
    path("products/", views.products, name="products"),
    path("about/", views.contact, name="about"),
    path("customer/<str:pk>/", views.customer, name="customer"),
    path("create_order/<str:pk>/", views.createOrder, name="create_order"),
    path("update_order/<str:pk_up>/", views.updateOrder, name="update_order"),
    path("delete_order/<str:pk_del>/", views.deleteOrder, name="delete_order"),
]