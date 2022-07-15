from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('gallery.html', views.artDisplay.as_view(), name='gallery.html'),
    path('contact.html', views.artDisplay.as_view(), name='contact.html'),
]