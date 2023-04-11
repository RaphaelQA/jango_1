from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)
    is_published = models.BooleanField()


class Category(models.Model):
    name = models.CharField(max_length=200)