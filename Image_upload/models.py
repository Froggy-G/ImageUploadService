from django.db import models
from taggit.managers import TaggableManager

class Image(models.Model):
    image = models.ImageField(upload_to='images')
    views = models.PositiveIntegerField(default=0)
    
    tags = TaggableManager()