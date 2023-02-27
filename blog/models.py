from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User,related_name='post_author' , on_delete=models.CASCADE , verbose_name=_('author'))
    title = models.CharField(max_length=50 , verbose_name=_('title'))
    description = models.TextField(max_length=10000 , verbose_name=_('description'))
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(_('image') ,upload_to='blog/')
    category = models.ForeignKey('Category', related_name='post_category', on_delete=models.CASCADE , verbose_name=_('category'))




class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
