from django.db import models

# Create your models here.
#model for blog post
class Post(models.Model):
    title=models.CharField(max_length=40)
    desc=models.TextField()
