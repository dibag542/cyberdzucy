from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=250)
    intro = models.TextField()
    full_text = models.TextField()

    def __str__(self):
        return self.name
