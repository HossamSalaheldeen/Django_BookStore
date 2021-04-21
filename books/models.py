from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2048)

    def __str__(self):
        return self.title