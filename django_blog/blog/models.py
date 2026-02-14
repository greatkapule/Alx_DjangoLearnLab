from django.db import models
from django.contrib.auth.models import User

class Post(models.py):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_backend=models.CASCADE)

    def __str__(self):
        return self.title