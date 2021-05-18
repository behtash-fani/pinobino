from django.urls import path
from . import views

app_name = 'pin'

urlpatterns = [
    path('', views.PinsListView.as_view(), name='listpin'),
    path('pin/<slug:slug>/', views.PinView.as_view(), name='single_pin'),
]