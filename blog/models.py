from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=200)
    post_date = models.DateField(auto_now=True, blank=True)
    author = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    description = models.TextField(help_text='Enter a blog description')

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])


class Blogger(models.Model):
    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    bio = models.TextField(help_text='Enter information about yourself')
    blogs = models.ForeignKey('Blog', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])


class Comment(models.Model):
    name = models.CharField(max_length=75)
    blog = models.ForeignKey('Blog', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(help_text='Enter your comment')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    post_date = models.DateField(auto_now=True, blank=True)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return self.name
