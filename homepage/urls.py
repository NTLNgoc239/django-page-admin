from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerPage, name="register"),

    # path('', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    # path('customer/<str:pk_test>/', views.customer, name="customer"),

    # path('create_store/<str:pk>/', views.createOrder, name="create_order"),
    path('update_store/<str:pk>/', views.updateStore, name="update_order"),
    path('delete_store/<str:pk>/', views.deleteStore, name="delete_order"),
    path('store/', views.stores, name='stores'),
    path('add_store/', views.addStore, name="add_store"),
    path('function_user/', views.functionUser, name="function_user")


]
