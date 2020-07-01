from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100, unique = True)
    message = models.TextField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
