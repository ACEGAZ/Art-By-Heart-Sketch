from django.shortcuts import render
from  django.views import generic
from .models import add_art


class artDisplay(generic.ListView):
    model = add_art
    template_name = 'index.html'
    paginate_by = 6
