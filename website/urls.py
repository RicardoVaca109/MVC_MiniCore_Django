from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_panel, name='panel_home'),
]
