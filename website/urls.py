from . import views
from django.urls import path

urlpatterns = [
    path('', views.artDisplay.as_view(), name='home')
]