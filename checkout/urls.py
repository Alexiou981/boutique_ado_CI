from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.checkout, name="checkout"),
    path('checktou_success/<order_number>', views.checkout_success, name="checkout_success"),
]
