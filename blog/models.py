from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Blogger(models.Model):
    name = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(help_text='Enter information about yourself')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])


class Blog(models.Model):
    title = models.CharField(max_length=200)
    post_date = models.DateField(auto_now=True)
    author = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True)
    description = models.TextField(help_text='Enter a blog description')

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    description = models.TextField(help_text='Enter comment about blog here')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        if len(self.description) > 75:
            comment_name = self.description[:75] + '...'
        else:
            comment_name = self.description
        return comment_name
