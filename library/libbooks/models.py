from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Books(models.Model):

    name = models.CharField(max_length=256)
    author = models.CharField(max_length=50)
    edition = models.IntegerField()
    publisher = models.CharField(max_length=256)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    #image = models.ImageField()

    def __unicode__(self):
        return ' : '.join([self.name, self.author])

