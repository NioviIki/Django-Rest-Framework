from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Posts(models.Model):
    subject = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject


class Comments(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.owner}: {self.text}'
