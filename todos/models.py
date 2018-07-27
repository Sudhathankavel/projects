from django.db import models
import datetime

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField('created date')

    def __str__(self):
        return self.title
