from django.db import models

# Create your models here.
class Members(models.Model):
    hobby = models.CharField(max_length=255)
    beskrivelse = models.CharField(max_length=255)
    