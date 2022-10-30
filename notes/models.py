from django.db import models
from django.forms import CharField

class Note(models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    body = models.TextField(null=True, help_text="Enter your notes here!")