from django.db import models


class Word(models.Model):
    title = models.CharField(max_length=255, unique=True)
    meanings = models.TextField()
    examples = models.TextField()

    def __str__(self):
        return self.title