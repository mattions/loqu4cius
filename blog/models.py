from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entry(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    body_text = models.TextField()
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.title
    