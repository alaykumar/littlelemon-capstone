from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('', views.home,name="home"),
    path('menu/', views.MenuItemsView.as_view()),
    #path('booking/',BookingViewSet),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    #path('booking/<int:pk>',SingleBookingView),
    
]