from django.db import models

class Product(models.Model):
    name = models.Charfield(max_length = 255)
    price = models.IntegerField()
    description = models.TextField()