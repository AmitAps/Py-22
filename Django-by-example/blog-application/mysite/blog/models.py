"""
Models for post.
"""

from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from django_quill.fields import QuillField


class Post(models.Model):
    """
    Post model. Define every filed related.
    """
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    #body = models.TextField()
    body = QuillField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        """
        Will return latest post.
        """
        ordering = ('-publish',)

    def __str__(self):
        """
        Return title in string format.
        """
        return str(self.title)
