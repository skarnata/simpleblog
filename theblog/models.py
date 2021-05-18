from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

"""
jika kita menggunakan default=timezone.now untuk field tipe DateField() kita tidak bisa bersamaan juga
menggunakan auto_now_add dan auto_now karena exclusively bertentangan
"""


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="Setiawan's blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='Coding')

    def __str__(self):
        """
        Disini kita menggunakan str() karena self.author adalah berbentuk object
        """
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id)))


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
