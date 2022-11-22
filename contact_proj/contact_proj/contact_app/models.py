from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=158)
    email = models.EmailField()
    subject = models.TextField(max_length=150, default='')
    message = models.TextField()
    query = models.TextField()


def __str__(self):
    return self.name
