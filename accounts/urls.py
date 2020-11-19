from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns=[
    path('',views.home),
    path('product/',views.product),
    path('customer/',views.customer)
]