from django.db import models
import datetime
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    posted = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.posted >= timezone.now() - datetime.timedelta(days=3)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    commenter = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    posted = models.DateTimeField('date published')

    def __str__(self):
        return "Comment by: " + str(self.commenter)


