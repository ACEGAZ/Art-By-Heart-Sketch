from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class add_art(models.Model):
    """add art to website from admin panel only"""
    title = models.CharField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()