from django.contrib import admin
from .models import add_art
from .models import Contact

admin.site.register(Contact)
admin.site.register(add_art)
