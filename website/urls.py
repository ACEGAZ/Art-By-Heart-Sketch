from django.urls import path
from . import views
from website import views as contact_views


urlpatterns = [
    path('', views.index, name='index'),
    path('gallery.html', views.ArtDisplay.as_view(), name='gallery.html'),
    path('contact.html', contact_views.contact_view, name='contact.html'),
]
