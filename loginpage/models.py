from django.db import models

# Create your models here.
class Flashcard(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    
    
class AILink(models.Model):
    url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.url
class ScrapedData(models.Model):
    column1 = models.CharField(max_length=255)
    column2 = models.CharField(max_length=255)