from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=500)
    
    def __str__(self):
        return f'{self.title}'
    