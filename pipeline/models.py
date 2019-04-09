from django.db import models

# Create your models here.

OBJECTS = (
  'Semicircle'
)

class Metadata(models.Model):
  image_name = models.CharField(max_length=200, blank=False, primary_key=True, unique=True)
  image_path = models.CharField(max_length=200)
  alphanumeric = models.CharField(max_length=1, blank=True, null=True)
  object = models.CharField(max_length=100, blank=True, null=True)
  alphanumeric_color = models.CharField(max_length=100, blank=True, null=True)
  shape_color = models.CharField(max_length=100, blank=True, null=True)
