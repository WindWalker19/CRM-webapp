from django.urls import path
from . import views

# app_name = 'accounts'

urlpatterns=[
    path('',views.home,name = "home"),
    path('product/',views.product,name = "product"),
    path('createCustomer/',views.createCustomer, name= "createCustomer"),
    #Making the Url dynamic.
    path('customer/<str:pk_test>/',views.customer, name = "customer"),
    path('createOrder/<str:pk>/',views.createOrder, name = "createOrder"),
    path('updateOrder/<str:pk>/',views.updateOrder, name = "updateOrder"),
    path('deleteOrder/<str:pk>/',views.deleteOrder, name = "deleteOrder")
]

