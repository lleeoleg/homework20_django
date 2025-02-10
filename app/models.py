from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    annotation = models.TextField()
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.title