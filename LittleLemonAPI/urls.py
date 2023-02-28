from django.urls import path
from . import views
from rest_framework import routers

urlpatterns = [
    path('menu-items/', views.SingleMenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
]