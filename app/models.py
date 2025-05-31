from django.db import models

from datetime import timedelta
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=False)

    def __str__(self):
        return self.title
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=False)
    published_date = models.DateTimeField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def published_recently(self):
        date_before = timezone.now() - timedelta(days=7) 

        return self.published_date >= date_before




