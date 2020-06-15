from django.db import models

class About(models.Model):
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

