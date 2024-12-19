from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='media/images', null=True, blank=True, verbose_name='Image')
    likes = models.ManyToManyField(User, related_name='Likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='Dislikes', blank=True)

    def __str__(self):
        return self.title, self.author, self.photo, self.likes, self.dislikes

    def number_of_likes(self):
        return self.likes.count()

    def number_of_dislikes(self):
        return self.dislikes.count()


class Comment(models.Model):
    advertisement = models.ForeignKey(Advertisement, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.advertisement}'